from tornado import web

from core import FM
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch


class SaveSessionHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def post(self):

        order = self.get_post('order')
        session = self.get_post('session')

        if order is None:
            self.json({
                'error': True,
                'message': 'no order provided'
            })
            self.finish()
            return

        if session is None:
            self.json({
                'error': True,
                'message': 'no session provided'
            })
            self.finish()
            return

        action = self.get_action(name=FM.Actions.SAVE_SESSION, session=session, order=order)
        response = action.run()

        self.json(response)
        self.finish()
