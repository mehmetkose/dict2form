#!/usr/bin/env python

import logging, os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

from dict2form import dict2form

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            debug=True,
            ui_modules= {
                "FormModule": FormModule,
            },
        )
        super(Application, self).__init__(handlers, **settings)


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        user = {'_id':'ID', 'slug':'myslug', 'name':'somebody', 'password':'123456'}
        self.render('page.html', user=user)

class FormModule(tornado.web.UIModule):

    def render(self, dictionary, name="object", method="POST", xsrf=None):
        hide = ['_id','slug','id']
        xsrf = xsrf.split('value="')[1].split('"')[0]
        return dict2form(dictionary, name=name, hide=hide, xsrf=xsrf)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
