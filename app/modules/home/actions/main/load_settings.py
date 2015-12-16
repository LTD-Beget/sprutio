from core import FM


class LoadSettings(FM.BaseAction):
    def __init__(self, request, **kwargs):
        super(LoadSettings, self).__init__(request=request, **kwargs)

    def run(self):
        rpc_request = self.get_rpc_request()

        result = rpc_request.request('main/load_settings', login=self.request.get_current_user(),
                                     password=self.request.get_current_password())
        answer = self.process_result(result)
        return answer
