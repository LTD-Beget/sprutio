from tornado import web

from core import FM
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch


class FtpCreateConnectionHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def post(self):

        params = self.get_post('params')

        if params is None:
            self.json({
                'error': True,
                'message': 'no params provided'
            })
            self.finish()
            return

        action = self.get_action(name=FM.Actions.FTP_CREATE, params=params)
        answer = action.run()

        self.json(answer)
        self.finish()
