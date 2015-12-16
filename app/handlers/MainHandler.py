from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch
from tornado import web


class MainHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def get(self):
        if self.application.options.debug:
            self.render("app.debug.html", language=self.get_current_language())
        else:
            self.render("app.html", language=self.get_current_language())
