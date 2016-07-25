from core import FM


class InitSession(FM.BaseAction):
    def __init__(self, request, session, path='/', **kwargs):
        super(InitSession, self).__init__(request=request, **kwargs)

        self.path = path
        self.session = session

    def run(self):
        request = self.get_rpc_request()
        result = request.request('main/init_session', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), path=self.path,
                                 session=self.session)
        answer = self.process_result(result)

        return answer

