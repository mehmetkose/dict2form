#!/usr/bin/env python
#-*- coding:utf-8 -*-


def generate_input(dict_object, key, hide, name):
    input_stack = ""
    if key in hide:
        return
    elif isinstance(dict_object[key], str) or isinstance(dict_object[key], unicode):
        label_str = "<label for='%s[%s]'>%s</label>" % (name, key, key)
        input_input = "<input name='%s[%s]' value='%s'><br />" % (
            name, key, dict_object[key])
        input_stack += "%s\n%s" % (label_str, input_input)
    elif isinstance(dict_object[key], dict):
        input_stack += "<div style='margin-left:1em;'>"
        input_stack += generate_inputs(dict_object[key], hide, name)
        input_stack += "</div>"
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
    print(result)
    return "%s\n%s\n%s" % (head, body, bottom)
