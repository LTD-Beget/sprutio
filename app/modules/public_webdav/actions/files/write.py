from core import FM
from core.FMOperation import FMOperation


class WriteFile(FM.BaseAction):
    def __init__(self, request, path, content, encoding, session, **kwargs):
        super(WriteFile, self).__init__(request=request, **kwargs)

        self.path = path
        self.content = content
        self.encoding = encoding
        self.session = session

    def run(self):
        request = self.get_rpc_request()
        result = request.request('webdav/write_file', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), path=self.path, content=self.content,
                                 encoding=self.encoding, session=self.session)
        answer = self.process_result(result)
        return answer

