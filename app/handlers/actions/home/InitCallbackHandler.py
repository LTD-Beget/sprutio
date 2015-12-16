from tornado import web
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch

from core import FM


class InitCallbackHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def post(self):

        action = self.get_action(name=FM.Actions.INIT_CALLBACK, module=FM.Modules.HOME)
        answer = action.run()

        self.json(answer)
        self.finish()
