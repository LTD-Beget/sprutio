import json

import redis
from config import server


class RedisConnector:
    def __init__(self):
        self.r = redis.StrictRedis(host=server.REDIS_DEFAULT_HOST, port=server.REDIS_DEFAULT_PORT,
                                   decode_responses=True)
        self.timeout = server.REDIS_DEFAULT_EXPIRE

    def set(self, key, value):
        try:
            status = self.setex(key, value, self.timeout)
            return status

        except Exception as e:
            msg = "Unable to connect to redis. " + str(e)
            raise Exception(msg)

    def setex(self, key, value, time):
        try:
            status = self.r.setex(key, time, value)
            return status
        except Exception as e:
            msg = "Unable to connect to redis." + str(e)
            raise Exception(msg)

    def lpush(self, key, *values):
        try:
            status = self.r.lpush(key, values)
            return status
        except Exception as e:
            msg = "Unable to connect to redis." + str(e)
            raise Exception(msg)

    def pipeline(self):
        try:
            pipe = self.r.pipeline()
            return pipe
        except Exception as e:
            raise Exception("Unable to connect to redis." + str(e))

    def incr(self, key, amount=1):
        try:
            status = self.r.incr(key, amount)
            return status
        except Exception as e:
            msg = "Unable to connect to redis." + str(e)
            raise Exception(msg)

    def set_list(self, key, list_value):
        try:
            value = json.dumps(list_value)
            status = self.r.set(key, value)
            return status
        except Exception as e:
            msg = "Unable to connect to redis." + str(e)
            raise Exception(msg)

    def get_list(self, key):
        try:
            status = json.loads(self.r.get(key))
            return status

        except Exception as e:
            msg = "Unable to connect to redis." + str(e)
            raise Exception(msg)

    def exists(self, key):
        try:
            status = self.r.exists(key)
            return status

        except Exception as e:
            msg = "Unable to connect to redis." + str(e)
            raise Exception(msg)

    def expire(self, key, seconds=-1):
        try:
            status = self.r.expire(key, seconds)
            return status
        except Exception as e:
            msg = "Unable to connect to redis." + str(e)
            raise Exception(msg)

    def delete(self, key):
        try:
            if self.exists(key) is True:
                status = self.r.delete(key)
            else:
                status = True
            return status

        except Exception as e:
            msg = "Unable to connect to redis." + str(e)
            raise Exception(msg)

    def get(self, key):
        try:
            status = self.r.get(key)
            return status
        except Exception as e:
            msg = "Unable to connect to redis." + str(e)
            raise Exception(msg)
