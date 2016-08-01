import json
import threading
import traceback
from config.settings import DEFAULT_COOKIE_TOKEN_NAME
from config.server import COOKIE_EXPIRE
from helpers import random_hash
from classes.core import FM


class FMAuth:
    @staticmethod
    def authenticate_by_pam(request, username, password):
        rpc_request = FM.BaseAction.get_rpc_request()

        result = rpc_request.request('main/authenticate', login=username, password=password)
        answer = FM.BaseAction.process_result(result)

        if not answer.get('Error', False) and answer.get('data').get('status', False):
            try:
                redis = request.redis.get(threading.currentThread())
                """:type : connectors.RedisConnector.RedisConnector"""
                token = 'FM::session::' + username + '::' + random_hash()
                params = {
                    "server": "localhost",
                    "user": username,
                    "password": password
                }
                redis.set(token, json.dumps(params))
                request.set_secure_cookie(DEFAULT_COOKIE_TOKEN_NAME, token, COOKIE_EXPIRE)
                return token
            except Exception as e:
                request.application.logger.error(
                    "Error in FMAuth: %s, traceback = %s" % (str(e), traceback.format_exc()))
                return False

        return False

    @staticmethod
    def authenticate_by_token(request, token):
        redis = request.redis.get(threading.currentThread())
        """:type : connectors.RedisConnector.RedisConnector"""
        if redis.exists(str(token)):
            try:
                params = redis.get(token)
                params = json.loads(str(params))
                redis.set(token, json.dumps(params))

                request.set_secure_cookie(DEFAULT_COOKIE_TOKEN_NAME, token, COOKIE_EXPIRE)
                return token
            except Exception as e:
                request.application.logger.error(
                    "Error in FMAuth: %s, traceback = %s" % (str(e), traceback.format_exc()))
                return False

        return False

    @staticmethod
    def logout(request):
        try:
            token = request.get_secure_cookie(DEFAULT_COOKIE_TOKEN_NAME)
            redis = request.redis.get(threading.currentThread())
            """:type : connectors.RedisConnector.RedisConnector"""

            redis.delete(request.get_current_user() + '::session')
            redis.delete(token)

            request.clear_cookie("token")
            request.clear_cookie("locale")
        except Exception as e:
            request.application.logger.error(
                "Error in FMAuth: %s, traceback = %s" % (str(e), traceback.format_exc()))
            return False
