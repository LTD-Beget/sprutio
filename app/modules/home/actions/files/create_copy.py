from core import FM
from core.FMOperation import FMOperation


class CreateCopy(FM.BaseAction):
    def __init__(self, request, paths, **kwargs):
        super(CreateCopy, self).__init__(request=request, **kwargs)

        self.paths = paths

    def run(self):
        request = self.get_rpc_request()

        operation = FMOperation.create(FM.Action.MOVE, FMOperation.STATUS_WAIT)
        result = request.request('home/create_copy', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), status_id=operation.id, paths=self.paths)
        answer = self.process_result(result)
        answer["data"] = operation.as_dict()
        return answer
