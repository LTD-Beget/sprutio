from core import FM


class NewFile(FM.BaseAction):
    def __init__(self, request, path, **kwargs):
        super(NewFile, self).__init__(request=request, **kwargs)

        self.path = path

    def run(self):
        request = self.get_rpc_request()

        result = request.request('home/new_file', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), path=self.path)
        answer = self.process_result(result)

        return answer
