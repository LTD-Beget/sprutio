import json

from core import FM


class SaveSession(FM.BaseAction):
    def __init__(self, request, order, session, **kwargs):
        super(SaveSession, self).__init__(request=request, **kwargs)

        self.order = order
        self.session = session

    def run(self):

        result = self.set_redis_session_data()
        return result

    def set_redis_session_data(self):

        redis_key = 'FM::session_state::' + self.request.get_current_user()
        redis = self.redis.get_current()

        if redis.exists(redis_key):
            session = json.loads(redis.get(redis_key))
        else:
            session = {}

        if 'Right' not in session:
            session = {
                'Right': {
                    'type': FM.Modules.HOME
                }
            }

        if 'Left' not in session:
            session = {
                'Left': {
                    'type': FM.Modules.HOME
                }
            }

        session[self.order] = self.session
        redis.set(redis_key, json.dumps(session))

        return {
            "message": "session saved"
        }
