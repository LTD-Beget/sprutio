import json
import random
import time
from datetime import datetime

from classes.connectors.RedisConnector import RedisConnector


class FMOperation(object):
    KEY_PREFIX = 'FM::Operation::'

    STATUS_WAIT = 'wait'
    STATUS_RUNNING = 'running'
    STATUS_SUCCESS = 'success'
    STATUS_ERROR = 'error'
    STATUS_ABORT = 'abort'

    def __init__(self):
        self.id = None
        self.login = None
        self.operation = None
        self.status = None
        self.data = None
        self.progress = None
        self.pid = None
        self.pname = None
        self.created_at = None
        self.updated_at = None

    @staticmethod
    def _get_key(operation_id):
        return FMOperation.KEY_PREFIX + operation_id

    @staticmethod
    def _generate_id():
        return str(time.time()) + ("%032x" % random.getrandbits(16))

    @staticmethod
    def load(operation_id, logger=None):
        redis = RedisConnector()
        redis_key = FMOperation._get_key(operation_id)
        if redis.exists(redis_key):
            attributes_json = redis.get(redis_key)
            attributes = json.loads(str(attributes_json))
            operation = FMOperation()
            operation.set_attributes(attributes)
            return operation
        else:
            if logger is not None:
                logger.error("Operation with %s not found" % operation_id)
            raise Exception("Operation with %s not found" % operation_id)

    def set_attributes(self, attributes):
        if isinstance(attributes, dict):
            self.id = attributes.get("id", self.id)
            self.login = attributes.get("login", self.login)
            self.operation = attributes.get("operation", self.operation)
            self.status = attributes.get("status", self.status)
            self.data = attributes.get("data", self.data)
            self.progress = attributes.get("progress", self.progress)
            self.pid = attributes.get("pid", self.pid)
            self.pname = attributes.get("pname", self.pname)
            self.created_at = attributes.get("created_at", self.created_at)
            self.updated_at = attributes.get("updated_at", self.updated_at)
        else:
            raise Exception("Attributes not a dict")

    def as_dict(self):
        return {
            "id": self.id,
            "login": self.login,
            "operation": self.operation,
            "status": self.status,
            "data": self.data,
            "progress": self.progress,
            "pid": self.pid,
            "pname": self.pname,
            "created_at": self.created_at,
            "update_at": self.updated_at,
        }

    @staticmethod
    def create(name, status):
        operation = FMOperation()
        operation.id = FMOperation._generate_id()
        operation.operation = name
        operation.status = status
        operation.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        operation.save()
        return operation

    def save(self):
        redis = RedisConnector()
        self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        redis.set(self._get_key(self.id), json.dumps(self.as_dict(), ensure_ascii=False))
