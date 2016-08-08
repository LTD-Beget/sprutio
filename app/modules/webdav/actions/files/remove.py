from core import FM
from core.FMOperation import FMOperation


class RemoveFiles(FM.BaseAction):
    def __init__(self, request, paths, session, **kwargs):
        super(RemoveFiles, self).__init__(request=request, **kwargs)

        self.paths = paths
        self.session = session

    def run(self):

        request = self.get_rpc_request()

        operation = FMOperation.create(FM.Action.REMOVE, FMOperation.STATUS_WAIT)
        result = request.request('webdav/remove_files', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), status_id=operation.id, paths=self.paths, session=self.session)
        answer = self.process_result(result)
        answer["data"] = operation.as_dict()
        return answer

