import json

from core import FM


class RestoreSession(FM.BaseAction):
    def __init__(self, request):
        super(RestoreSession, self).__init__(request=request)

    def run(self):
        session = self.get_redis_session_data()

        if session is not None:
            same = False

            same_path = (session['Right']['path'] == session['Left']['path'])
            same_type = (session['Right']['type'] == session['Left']['type'])

            if same_type and same_path:
                if session['Left']['type'] == FM.Modules.WEBDAV:
                    if session['Left']['server_id'] == session['Left']['server_id']:
                        same = True
                if session['Left']['type'] == FM.Modules.SFTP:
                    if session['Left']['server_id'] == session['Left']['server_id']:
                        same = True
                if session['Left']['type'] == FM.Modules.FTP:
                    if session['Left']['server_id'] == session['Left']['server_id']:
                        same = True
                if session['Left']['type'] == FM.Modules.HOME:
                    same = True

            message = {
                "session": session,
                "same": same,
                "restore": True
            }
        else:
            message = {
                "restore": False
            }

        return {
            "data": message
        }

    def get_redis_session_data(self):

        redis_key = 'FM::session_state::' + self.request.get_current_user()
        redis = self.redis.get_current()

        if not redis.exists(redis_key):
            return None

        session = json.loads(redis.get(redis_key))

        if ('Right' not in session) or ('Left' not in session):
            return None

        # Fill default values
        if 'type' not in session['Right']:
            session['Right']['type'] = FM.Modules.HOME

        if 'type' not in session['Left']:
            session['Left']['type'] = FM.Modules.HOME

        return session
