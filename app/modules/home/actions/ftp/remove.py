from core import FM


class RemoveFtp(FM.BaseAction):
    def __init__(self, request, params, **kwargs):
        super(RemoveFtp, self).__init__(request=request, **kwargs)

        self.params = params

    def run(self):
        request = self.get_rpc_request()

        result = request.request('ftp/remove_connection', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), connection_id=self.params.get('id'))
        answer = self.process_result(result)

        return answer
