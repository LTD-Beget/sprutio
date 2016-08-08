from core import FM


class UpdateWebDav(FM.BaseAction):
    def __init__(self, request, params, **kwargs):
        super(UpdateWebDav, self).__init__(request=request, **kwargs)

        self.params = params

    def run(self):
        request = self.get_rpc_request()

        result = request.request('webdav/edit_connection', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), connection_id=self.params.get('id'),
                                 host=self.params.get('host'), webdav_user=self.params.get('user'),
                                 webdav_password=self.params.get('password'))
        answer = self.process_result(result)
        return answer
