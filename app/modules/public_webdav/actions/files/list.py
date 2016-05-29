from core import FM


class ListFiles(FM.BaseAction):
    def __init__(self, request, path, session, **kwargs):
        super(ListFiles, self).__init__(request=request, **kwargs)

        self.path = path
        self.session = session

    def run(self):
        request = self.get_rpc_request()

        result = request.request('webdav/list_files', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), path=self.path, session=self.session)
        answer = self.process_result(result)
        return answer

