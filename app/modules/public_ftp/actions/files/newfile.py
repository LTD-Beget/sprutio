from core import FM


class NewFile(FM.BaseAction):
    def __init__(self, request, path, session, **kwargs):
        super(NewFile, self).__init__(request=request, **kwargs)

        self.path = path
        self.session = session

    def run(self):
        request = self.get_rpc_request()
        result = request.request('ftp/new_file', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), path=self.path, session=self.session)
        answer = self.process_result(result)

        return answer
