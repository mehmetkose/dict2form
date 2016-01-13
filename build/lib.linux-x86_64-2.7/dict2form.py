#!/usr/bin/env python
#-*- coding:utf-8 -*-


def generate_inputs(dict_object, hide, name):
	body = ""
	for key in dict_object.keys():
		if key in hide:
			continue
		elif isinstance(dict_object[key], str) or isinstance(dict_object[key], unicode):
			label = "<label for='%s[%s]'>%s</label>" % (name, key, key)
			input_str = "<input name='%s[%s]' value='%s'><br />" % (name, key, dict_object[key])
			body += "%s\n%s" % (label,input_str)
		# elif isinstance(dict_object[key], dict):
		# 	body += generate_inputs(dict_object[key], hide, name, sub=key)
	return body


def dict2form(dict_object, name="object", hide=[], method="get", xsrf=None, submit_name="Submit"):
	head = "<form enctype='application/json' method='%s'>" % method
	body = "<input type='submit' value='%s'>" % (submit_name)
	bottom = "</form>"
	if xsrf:
		body += '<input type="hidden" name="_xsrf" value="%s"/>' % xsrf
	body = "%s%s" % (generate_inputs(dict_object, hide, name), body)
	return "%s\n%s\n%s" % (head, body, bottom)


