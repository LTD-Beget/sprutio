from tornado import web

from core import FM
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch


class ArchiveCreateHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def post(self):

        params = self.get_post('params')
        session = self.get_post('session')

        if params is None:
            self.json({
                'error': True,
                'message': 'no params provided'
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

        action = self.get_action(name=FM.Actions.CREATE_ARCHIVE, module=session.get('type'), params=params,
                                 session=session)
        answer = action.run()

        self.json(answer)
        self.finish()
