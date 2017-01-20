from tornado import web

from core import FM
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch


class InitCallbackHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def post(self):

        action = self.get_action(name=FM.Actions.INIT_CALLBACK, module=FM.Modules.HOME)
        answer = action.run()

        self.json(answer)
        self.finish()
