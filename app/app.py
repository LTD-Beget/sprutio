import logging

import tornado.httpserver

from classes.bootstrap import Bootstrap
from config import server, routes, console
from config import settings

options = console.parse_options()


class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__(routes.HANDLERS, **settings.SETTINGS)
        bootstrap = Bootstrap(self, options)
        bootstrap.run()

if __name__ == "__main__":
    tornado.log.enable_pretty_logging()
    logging.info("starting Tornado web server")
    http_server = tornado.httpserver.HTTPServer(
        Application(),
        xheaders=server.XHEADERS,
        max_buffer_size=server.MAX_BUFFER_SIZE,
        max_body_size=server.MAX_BUFFER_SIZE,
        chunk_size=server.CHUNK_SIZE,
        idle_connection_timeout=server.IDLE_CONNECTION_TIMEOUT,
        body_timeout=server.BODY_TIMEOUT)
    http_server.listen(options.port, address=options.host)
    tornado.ioloop.IOLoop.instance().start()
