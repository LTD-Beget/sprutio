from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch
from classes.core.FMLocale import FMLocale
from config import settings
from tornado import web


class MainHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def get(self):
        language = self.get_argument("language", None)
        if language is not None:
            secure_cookie = self.get_secure_cookie(settings.DEFAULT_COOKIE_TOKEN_NAME)
            auth_key = bytes.decode(secure_cookie)

            if language not in settings.LANGUAGES:
                language = settings.DEFAULT_LANGUAGE

            FMLocale.set_language(self, language, auth_key)
        if self.application.options.debug:
            self.render("app.debug.html", language=self.get_current_language())
        else:
            self.render("app.html", language=self.get_current_language())
