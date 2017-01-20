from tornado import web

from core import FM
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch


class CancelOperationHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def post(self):

        status = self.get_post('status')
        session = self.get_post('session')

        if status is None:
            self.json({
                'error': True,
                'message': 'no status provided'
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

        action = self.get_action(name=FM.Actions.CANCEL_OPERATION, module=session['type'],
                                 status=status, session=session)
        answer = action.run()

        self.json(answer)
        self.finish()
