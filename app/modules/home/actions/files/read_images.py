from core import FM
from config.server import IDLE_CONNECTION_TIMEOUT


class ReadImages(FM.BaseAction):
    def __init__(self, request, paths, **kwargs):
        super(ReadImages, self).__init__(request=request, **kwargs)

        self.paths = paths

    def run(self):
        request = self.get_rpc_request()
        request.set_timeout(IDLE_CONNECTION_TIMEOUT)
        result = request.request('home/read_images', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), paths=self.paths)
        answer = self.process_result(result)
        return answer
