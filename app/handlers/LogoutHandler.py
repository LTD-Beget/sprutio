import tornado.escape
import tornado.locale
import tornado.web

from classes.core.FMAuth import FMAuth
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch


class LogoutHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    def get(self):
        try:
            FMAuth.logout(self)
            self.redirect(self.get_login_url(), False)

        except Exception as e:
            raise tornado.web.HTTPError(403, "Authentication Failed " + str(e))

    @wrap_async_rpc
    @wrap_catch
    def post(self):
        try:
            FMAuth.logout(self)
            self.redirect(self.get_login_url(), False)

        except Exception as e:
            raise tornado.web.HTTPError(403, "Authentication Failed " + str(e))
