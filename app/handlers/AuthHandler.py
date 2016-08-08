from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch
from classes.core.FMLocale import FMLocale
from classes.core.FMAuth import FMAuth
from config import settings

import tornado.web
import tornado.escape
import tornado.locale


class AuthHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    def get(self):
        try:
            token = self.get_argument("authkey", None)
            language = self.get_argument("language", settings.DEFAULT_LANGUAGE)

            if language not in settings.LANGUAGES:
                language = settings.DEFAULT_LANGUAGE

            if token is not None:
                session_token = FMAuth.authenticate_by_token(self, token)
                if session_token:
                    FMLocale.set_language(self, language, session_token)
                    self.redirect('/')
                else:
                    raise Exception("Session key is not exist")
            else:
                raise Exception("Session key is not provided")

        except Exception as e:
            self.application.logger.error('In AuthHandler Exception: ' + str(e))
            raise tornado.web.HTTPError(403, "Authentication Failed")

    @wrap_async_rpc
    @wrap_catch
    def post(self):
        try:
            token = self.get_argument("authkey", None)
            language = self.get_argument("language", settings.DEFAULT_LANGUAGE)

            login = self.get_argument("login", None)
            password = self.get_argument("password", None)

            if language not in settings.LANGUAGES:
                language = settings.DEFAULT_LANGUAGE

            if token is not None:
                session_token = FMAuth.authenticate_by_token(self, token)
                if session_token:
                    FMLocale.set_language(self, language, session_token)
                    self.json({
                        'error': False,
                        'url': '/'
                    })
                else:
                    self.json({
                        'error': True,
                        'message': self.get_user_locale().translate("Incorrect security token")
                    })
            else:
                session_token = FMAuth.authenticate_by_pam(self, login, password)
                if session_token:
                    FMLocale.set_language(self, language, session_token)
                    self.json({
                        'error': False,
                        'url': '/'
                    })
                else:
                    self.json({
                        'error': True,
                        'message': self.get_user_locale().translate("Incorrect login or password")
                    })

            self.finish()

        except Exception as e:
            self.application.logger.error('In AuthHandler Exception: ' + str(e))
            raise tornado.web.HTTPError(403, "Authentication Failed")

    def write_error(self, status_code, **kwargs):
        self.application.logger.error('In AuthHandler status_code: ', status_code)
        if status_code == 403:
            self.redirect(self.get_login_url())
        elif status_code in [403, 404, 500, 503]:
            self.write('Error %s' % status_code)
        else:
            self.write('Unknown Error')
