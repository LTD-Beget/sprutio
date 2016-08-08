from core import FM


class RemoveWebDav(FM.BaseAction):
    def __init__(self, request, params, **kwargs):
        super(RemoveWebDav, self).__init__(request=request, **kwargs)

        self.params = params

    def run(self):
        request = self.get_rpc_request()

        result = request.request('webdav/remove_connection', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), connection_id=self.params.get('id'))
        answer = self.process_result(result)

        return answer
