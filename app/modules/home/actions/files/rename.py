from core import FM


class RenameFile(FM.BaseAction):
    def __init__(self, request, source_path, target_path, **kwargs):
        super(RenameFile, self).__init__(request=request, **kwargs)

        self.source_path = source_path
        self.target_path = target_path

    def run(self):
        request = self.get_rpc_request()

        result = request.request('home/rename_file', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), source_path=self.source_path,
                                 target_path=self.target_path)
        answer = self.process_result(result)

        return answer
