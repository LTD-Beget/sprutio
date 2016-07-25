from core import FM
from config.server import IDLE_CONNECTION_TIMEOUT


class UploadFile(FM.BaseAction):
    def __init__(self, request, session, file_path, overwrite, **kwargs):
        super(UploadFile, self).__init__(request=request, **kwargs)

        self.path = session.get('path')
        self.file_path = file_path
        self.overwrite = overwrite
        self.session = session

    def run(self):
        request = self.get_rpc_request()
        request.set_timeout(IDLE_CONNECTION_TIMEOUT)
        result = request.request('ftp/upload_file', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), path=self.path, file_path=self.file_path,
                                 overwrite=self.overwrite, session=self.session)
        answer = self.process_result(result)
        return answer
