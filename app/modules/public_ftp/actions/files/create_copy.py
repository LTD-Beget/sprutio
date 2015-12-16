from core import FM
from core.FMOperation import FMOperation


class CreateCopy(FM.BaseAction):
    def __init__(self, request, paths, session, **kwargs):
        super(CreateCopy, self).__init__(request=request, **kwargs)

        self.paths = paths
        self.session = session

    def run(self):
        request = self.get_rpc_request()

        operation = FMOperation.create(FM.Action.CREATE_COPY, FMOperation.STATUS_WAIT)

        result = request.request('ftp/create_copy', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), status_id=operation.id,
                                 paths=self.paths, session=self.session)

        answer = self.process_result(result)
        answer["data"] = operation.as_dict()
        return answer
