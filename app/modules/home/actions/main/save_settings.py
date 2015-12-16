from core import FM


class SaveSettings(FM.BaseAction):
    def __init__(self, request, params, **kwargs):
        super(SaveSettings, self).__init__(request=request, **kwargs)

        self.params = params

    def run(self):
        rpc_request = self.get_rpc_request()
        result = rpc_request.request('main/save_settings', login=self.request.get_current_user(),
                                     password=self.request.get_current_password(), params=self.params)
        answer = self.process_result(result)
        return answer
