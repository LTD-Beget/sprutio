from tornado import web

from core import FM
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch


class RenameFileHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def post(self):

        session = self.get_post('session')
        source_path = self.get_post('source_path')
        target_path = self.get_post('target_path')

        if source_path is None:
            self.json({
                'error': True,
                'message': 'no source path provided'
            })
            self.finish()
            return

        if target_path is None:
            self.json({
                'error': True,
                'message': 'no target path provided'
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

        action = self.get_action(name=FM.Actions.RENAME_FILE, module=session.get('type'), source_path=source_path,
                                 target_path=target_path, session=session)
        answer = action.run()

        self.json(answer)
        self.finish()
