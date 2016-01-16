#!/usr/bin/env python
#-*- coding:utf-8 -*-

# python dictionary object to html5 json form generator.
# https://github.com/mehmetkose/dict2form

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2016 Mehmet Kose mehmetkose.py@gmail.com


def generate_input(dict_object, key, hide, name):
    input_stack = ""
    if key in hide:
        return
    elif isinstance(dict_object[key], str) or isinstance(dict_object[key], unicode):
        label_str = "<label for='%s[%s]'>%s</label>" % (name, key, key)
        input_str = "<input name='%s[%s]' value='%s'>\n" % (
            name, key, dict_object[key])
        input_stack += "%s\n%s" % (label_str, input_str)
    elif isinstance(dict_object[key], list):
        label_str = "<label for='%s[%s]'>%s</label>" % (name, key, key)
        input_str = ""
        for value in [item for item in enumerate(dict_object[key])]:
            input_str += "<input name='%s[%s][%s]' value='%s'>\n" % (
                name, key, value[0], value[1])
        input_stack += "%s\n%s" % (label_str, input_str)
    elif isinstance(dict_object[key], dict):
        input_stack += "<div class='sub'>\n"
        input_stack += generate_inputs(dict_object[key], hide, name)
        input_stack += "</div>\n"
    return input_stack


def generate_inputs(dict_object, hide, name):
    body = ""
    for key in dict_object.keys():
        body += generate_input(dict_object, key, hide, name)
    return body


def dict2form(dict_object, name="object", hide=[], method="get", xsrf=None, submit_name="Submit"):
    head = "<form enctype='application/json' method='%s'>" % method
    body = "<input type='submit' value='%s'>" % (submit_name)
    bottom = "</form>"
    if xsrf:
        body += '<input type="hidden" name="_xsrf" value="%s"/>' % xsrf
    body = "%s%s" % (generate_inputs(dict_object, hide, name), body)
    result = "%s\n%s\n%s" % (head, body, bottom)
    return "%s\n%s\n%s" % (head, body, bottom)
