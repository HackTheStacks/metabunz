#!/usr/bin/env python
import logging

import tornado.httpserver
import tornado.httpclient
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.gen


class HealthHandler(tornado.web.RequestHandler):
    def get(self):
        self.finish('OK')


class Application(tornado.web.Application):
    def __init__(self):
        app_settings = {
            'debug': True,
        }

        app_handlers = [
            (r'^/health/?$', HealthHandler),
        ]
        super(Application, self).__init__(app_handlers, **app_settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()

    port = 12040
    address = '0.0.0.0'
    logging.info('starting on %s:%d', address, port)

    http_server = tornado.httpserver.HTTPServer(
        request_callback=Application(), xheaders=True)
    http_server.listen(port, address=address)

    tornado.ioloop.IOLoop.instance().start()
