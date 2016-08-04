from tornado import web
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch

from core import FM


class InitSessionHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def post(self):
        session = self.get_post('session', {
            'type': FM.Modules.HOME,
            'host': self.get_current_host(),
            'path': None
        })
        action = self.get_action(name=FM.Actions.INIT_SESSION, module=session['type'],
                                 path=session['path'], session=session)
        answer = action.run()

        self.json(answer)
        self.finish()
