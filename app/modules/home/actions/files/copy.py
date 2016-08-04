from core import FM
from core.FMOperation import FMOperation


class CopyFiles(FM.BaseAction):
    def __init__(self, request, paths, session, target, overwrite, **kwargs):
        super(CopyFiles, self).__init__(request=request, **kwargs)

        self.paths = paths
        self.session = session
        self.target = target
        self.overwrite = overwrite

    def run(self):
        request = self.get_rpc_request()

        operation = FMOperation.create(FM.Action.COPY, FMOperation.STATUS_WAIT)

        result = request.request('home/copy_files', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), status_id=operation.id,
                                 source=self.session, target=self.target, paths=self.paths, overwrite=self.overwrite)

        answer = self.process_result(result)
        answer["data"] = operation.as_dict()
        return answer
