from tornado import web

from core import FM
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch


class RestoreSessionHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def post(self):
        action = self.get_action(name=FM.Actions.RESTORE_SESSION)
        response = action.run()

        self.json(response)
        self.finish()
