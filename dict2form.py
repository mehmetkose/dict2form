#!/usr/bin/env python
#-*- coding:utf-8 -*-


def generate_inputs(dict_object, hide, name, sub=None):
	body = ""
	for key in dict_object.keys():
		if key in hide:
			continue
		elif isinstance(dict_object[key], str) or isinstance(dict_object[key], unicode):
			label = "<label for='%s[%s]'>%s</label>" % (name, key, key)
			input_str = "<input name='%s[%s]' value='%s'><br />" % (name, key, dict_object[key])
			body += "\n%s\n%s" % (label,input_str)
			if sub:
				print("\n\n\n##############")
				replace_from = "%s[" % (name)
				replace_to = "%s[%s][" % (name,sub)
				body.replace(replace_from, replace_to)
				print(body)
		elif isinstance(dict_object[key], dict):
			body += generate_inputs(dict_object[key], hide, name, sub=key)
	return body


def dict2form(dict_object, name="object", hide=[], method="get", xsrf=None):
	head = "<form enctype='application/json' method='%s'>" % method
	body = ""
	bottom = "</form>"
	if xsrf:
		body += '<input type="hidden" name="_xsrf" value="%s"/>' % xsrf
	body += generate_inputs(dict_object, hide, name)
	return "%s\n%s\n%s" % (head, body, bottom)


