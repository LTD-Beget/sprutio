from core import FM


class CancelOperation(FM.BaseAction):
    def __init__(self, request, status, **kwargs):
        super(CancelOperation, self).__init__(request=request, **kwargs)

        self.status = status

    def run(self):
        request = self.get_rpc_request()

        result = request.request('main/cancel_operation', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), status_id=self.status.get('id'))
        answer = self.process_result(result)

        return answer

