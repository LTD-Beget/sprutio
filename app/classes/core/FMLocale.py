import json
import threading

from tornado import locale

from config.settings import LOCALES, DEFAULT_LANGUAGE, DEFAULT_LOCALE


class FMLocale:
    @staticmethod
    def set_language(request, language, session=None):
        locale.set_default_locale(LOCALES.get(language, DEFAULT_LANGUAGE))
        request.set_secure_cookie('locale', LOCALES.get(language, DEFAULT_LANGUAGE), 1)
        request.locale = locale.get(LOCALES.get(language, DEFAULT_LOCALE))

        if session is not None and session is not False:
            redis = request.redis.get(threading.currentThread())
            """:type : connectors.RedisConnector.RedisConnector"""
            if redis.exists(str(session)):
                params = redis.get(session)
                params = json.loads(str(params))
                params["language"] = language
                redis.set(session, json.dumps(params))
