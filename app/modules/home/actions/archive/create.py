from core import FM
from core.FMOperation import FMOperation


class CreateArchive(FM.BaseAction):
    def __init__(self, request, params, **kwargs):
        super(CreateArchive, self).__init__(request=request, **kwargs)

        self.params = params

    def run(self):
        request = self.get_rpc_request()
        operation = FMOperation.create(FM.Action.CREATE_ARCHIVE, FMOperation.STATUS_WAIT)

        result = request.request('home/create_archive', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), status_id=operation.id, params=self.params)
        answer = self.process_result(result)
        answer["data"] = operation.as_dict()
        return answer
