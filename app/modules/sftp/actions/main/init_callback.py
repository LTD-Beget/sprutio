from core import FM


class InitCallback(FM.BaseAction):
    def __init__(self, request, **kwargs):
        super(InitCallback, self).__init__(request=request, **kwargs)

    def run(self):
        request = self.get_rpc_request()

        result = request.request('main/init_callback', login=self.request.get_current_user(),
                                 password=self.request.get_current_password())
        answer = self.process_result(result)

        return answer
