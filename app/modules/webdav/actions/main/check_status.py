from core import FM
from core.FMOperation import FMOperation


class CheckStatus(FM.BaseAction):
    def __init__(self, request, status, **kwargs):
        super(CheckStatus, self).__init__(request=request, **kwargs)

        self.status = status

    def run(self):
        try:
            operation = FMOperation.load(self.status.get('id'))
            answer = {
                "error": False,
                "message": "",
                "data": operation.as_dict()
            }
        except Exception as e:
            answer = {
                "error": True,
                "message": str(e)
            }

        return answer

