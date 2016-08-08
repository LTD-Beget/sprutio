from core import FM
from core.FMOperation import FMOperation


class AnalyzeSize(FM.BaseAction):
    def __init__(self, request, path, session, **kwargs):
        super(AnalyzeSize, self).__init__(request=request, **kwargs)

        self.path = path
        self.session = session

    def run(self):
        request = self.get_rpc_request()

        operation = FMOperation.create(FM.Action.ANALYZE_SIZE, FMOperation.STATUS_WAIT)
        result = request.request('sftp/analyze_size', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), status_id=operation.id,
                                 path=self.path, session=self.session)
        answer = self.process_result(result)
        answer["data"] = operation.as_dict()
        return answer
