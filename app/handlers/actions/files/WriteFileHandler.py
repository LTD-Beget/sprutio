from tornado import web

from core import FM
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch


class WriteFileHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def post(self):

        path = self.get_post('path')
        session = self.get_post('session')
        content = self.get_post('content')
        encoding = self.get_post('encoding')

        if path is None:
            self.json({
                'error': True,
                'message': 'no path provided'
            })
            self.finish()
            return

        if encoding is None:
            self.json({
                'error': True,
                'message': 'no encoding provided'
            })
            self.finish()
            return

        if content is None:
            self.json({
                'error': True,
                'message': 'no content provided'
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

        action = self.get_action(name=FM.Actions.WRITE_FILE, module=session.get('type'), path=path, session=session,
                                 content=content, encoding=encoding)
        answer = action.run()

        self.json(answer)
        self.finish()
