from core import FM


class WriteFile(FM.BaseAction):
    def __init__(self, request, path, content, encoding, **kwargs):
        super(WriteFile, self).__init__(request=request, **kwargs)

        self.path = path
        self.content = content
        self.encoding = encoding

    def run(self):
        request = self.get_rpc_request()

        result = request.request('home/write_file', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), path=self.path, content=self.content,
                                 encoding=self.encoding)
        answer = self.process_result(result)
        return answer
