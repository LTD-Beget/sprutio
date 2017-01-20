import threading

from connectors.RedisConnector import RedisConnector


class RedisPool:

    pool = dict()

    def get_current(self):
        return self.get(threading.current_thread())

    def close_current(self):
        return self.close(threading.current_thread())

    def get(self, thread):

        key = thread.ident

        # Get from pool stack
        if key in self.pool.keys():
            return self.pool[key]
        else:
            self.pool[key] = RedisConnector()

        return self.pool[key]

    def close(self, thread):
        key = thread.ident

        # Clean pool stack with closing connection
        if key in self.pool.keys():
            del self.pool[key]