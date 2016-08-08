import threading
import tornado.web
import tornado.escape
import tornado.locale
import json
import traceback
import logging
from core import FM
from config.settings import DEFAULT_LOCALE, DEFAULT_LANGUAGE, DEFAULT_COOKIE_TOKEN_NAME
from config import server


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application=application, request=request, **kwargs)

    def initialize(self):
        pass

    def data_received(self, chunk):
        pass

    @property
    def config(self):
        return self.application.config

    @property
    def redis(self):
        return self.application.redis

    def json(self, data=None, code=200):
        self.set_status(code)
        self.set_header("Content-Type", "application/json; charset=UTF-8")

        if isinstance(data, dict) and data.get("error", False):
            self.set_status(500)

        try:
            answer = json.dumps(data, ensure_ascii=False)
        except TypeError:
            self.set_status(500)
            self.application.logger.error(
                "login:" + self.get_current_user() + ' -- Traceback:' + traceback.format_exc())
            answer = {
                "error": True,
                "message": "Serialization error"
            }

        self.write(answer)

    def on_finish(self):
        self.redis.close_current()

    def _handle_request_exception(self, e):
        self.application.logger.error("Handled exception in app.py: " + str(e) + "Traceback:" + traceback.format_exc())
        if isinstance(e, tornado.web.HTTPError):
            if e.status_code == 403:
                self.set_status(e.status_code)
                self.application.logger.error("login: None -- Traceback:" + traceback.format_exc())
                self.write('Error %s' % e.status_code)
                self.redirect(self.get_login_url())
            elif e.status_code in [404, 500, 503]:
                self.set_status(e.status_code)
                self.write('Error %s' % e.status_code)
        else:
            self.application.logger.error(
                "login:" + self.get_current_user() + ' -- Traceback:' + traceback.format_exc())
            self.set_status(500)
            self.write(json.dumps({'message': str(e)}, ensure_ascii=False))

        if not self._finished:
            self.finish()

    def get_post(self, key, default=None):

        body = self.request.body.decode('utf-8')

        if body == '':
            return default

        try:
            data = json.loads(body)
        except ValueError:
            self.application.logger.error(
                "JSON DECODE ERROR login:" + self.get_current_user() + ' -- Traceback:' + traceback.format_exc())
            return default

        if isinstance(data, dict):
            return data.get(key, default)
        else:
            return default

    def get_current_language(self):

        redis = self.redis.get(threading.currentThread())
        secure_cookie = self.get_secure_cookie(DEFAULT_COOKIE_TOKEN_NAME)

        if secure_cookie is None:
            return DEFAULT_LANGUAGE

        auth_key = bytes.decode(secure_cookie)
        params = redis.get(auth_key)

        if params is None:
            return DEFAULT_LANGUAGE

        params = json.loads(params)
        redis.expire(auth_key, 86400)

        return params.get("language", DEFAULT_LANGUAGE)

    def get_current_user(self):
        redis = self.redis.get(threading.currentThread())
        secure_cookie = self.get_secure_cookie("token")

        if secure_cookie is None:
            return None

        auth_key = bytes.decode(secure_cookie)
        params = redis.get(auth_key)

        if params is None:
            return None

        params = json.loads(params)
        redis.expire(auth_key, server.REDIS_DEFAULT_EXPIRE)

        return params.get("user", None)

    def get_error(self, e, msg=""):
        self.application.logger.error(
            "Error in FM Main: %s, %s, traceback = %s" % (msg, str(e), traceback.format_exc()))

        result = {
            "error": True,
            "message": msg,
        }

        if self.application.options.debug:
            result['traceback'] = traceback.format_exc()
            result['message'] += ' ' + str(e)

        return result

    def get_action(self, name, *args, **kwargs):
        action = FM.ActionsProvider.get_action(action_name=name, request=self, *args, **kwargs)
        return action

    def get_beget_path(self):
        login = self.get_current_user()
        return '/home/' + login[0] + '/' + login

    def get_current_host(self):
        redis = self.redis.get(threading.currentThread())
        secure_cookie = self.get_secure_cookie("token")

        if secure_cookie is None:
            raise tornado.web.HTTPError(403, "Authentication Failed")

        auth_key = bytes.decode(secure_cookie)
        params = redis.get(auth_key)

        if params is None:
            raise tornado.web.HTTPError(403, "Authentication Failed")

        redis.expire(auth_key, 86400)
        params = json.loads(params)

        return params['server']

    def get_current_password(self):

        redis = self.redis.get(threading.currentThread())
        secure_cookie = self.get_secure_cookie("token")

        if secure_cookie is None:
            raise tornado.web.HTTPError(403, "Authentication Failed")

        auth_key = bytes.decode(secure_cookie)
        params = redis.get(auth_key)

        if params is None:
            raise tornado.web.HTTPError(403, "Authentication Failed")

        redis.expire(auth_key, 86400)
        params = json.loads(params)

        return params['password']

    def get_user_locale(self):
        try:
            locale = bytes.decode(self.get_secure_cookie("locale"))
            if locale:
                return tornado.locale.get(locale)
        except:
            return tornado.locale.get(DEFAULT_LOCALE)


def wrap_catch(method):
    def catch(*args, **kwargs):

        self = args[0]
        try:
            return method(*args, **kwargs)

        except Exception as e:
            msg = "Catched Error in FM Main request thread"
            logger = logging.getLogger('tornado.application')
            logger.error("Error in FM Main: %s, %s, traceback = %s" % (msg, str(e), traceback.format_exc()))

            self.redis.close(threading.currentThread())
            self._handle_request_exception(e)

    return catch


def wrap_async_rpc(method):
    @tornado.web.asynchronous
    def run(*args, **kwargs):

        self = args[0]
        try:
            threading.Thread(target=method, args=args, kwargs=kwargs).start()

        except Exception as e:
            msg = "Catched Error in FM Main request thread"
            logger = logging.getLogger('tornado.application')
            logger.error("Error in FM Main: %s, %s, traceback = %s" % (msg, str(e), traceback.format_exc()))

            self.redis.close(threading.currentThread())
            self._handle_request_exception(e)

    return run
