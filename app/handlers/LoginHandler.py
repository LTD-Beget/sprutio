from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch
from config.settings import DEFAULT_LANGUAGE, LANGUAGES
from classes.core.FMLocale import FMLocale


class LoginHandler(BaseHandler):
    @wrap_async_rpc
    @wrap_catch
    def get(self):
        language = self.get_argument("language", DEFAULT_LANGUAGE)
        if language not in LANGUAGES:
            language = DEFAULT_LANGUAGE

        FMLocale.set_language(self, language)

        if self.application.options.debug:
            self.render("login.html", language=language)
        else:
            self.render("login.html", language=language)
