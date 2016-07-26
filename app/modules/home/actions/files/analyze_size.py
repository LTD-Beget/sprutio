from core import FM
from core.FMOperation import FMOperation


class AnalyzeSize(FM.BaseAction):
    def __init__(self, request, path, **kwargs):
        super(AnalyzeSize, self).__init__(request=request, **kwargs)

        self.path = path

    def run(self):
        request = self.get_rpc_request()

        operation = FMOperation.create(FM.Action.ANALYZE_SIZE, FMOperation.STATUS_WAIT)
        result = request.request('home/analyze_size', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), status_id=operation.id, path=self.path)
        answer = self.process_result(result)
        answer["data"] = operation.as_dict()
        return answer
