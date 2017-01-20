from tornado import web

from core import FM
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch


class SaveRulesHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def post(self):

        path = self.get_post('path')
        session = self.get_post('session')
        params = self.get_post('params')

        if path is None:
            self.json({
                'error': True,
                'message': 'no path provided'
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

        if params is None:
            self.json({
                'error': True,
                'message': 'no params provided'
            })
            self.finish()
            return

        action = self.get_action(name=FM.Actions.HTACCESS_SAVE_RULES, module=session.get('type'), path=path,
                                 session=session, params=params)
        answer = action.run()

        self.json(answer)
        self.finish()
