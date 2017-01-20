from tornado import web

from core import FM
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch


class CopyFilesHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def post(self):

        paths = self.get_post('paths')
        session = self.get_post('session')
        target = self.get_post('target')
        overwrite = self.get_post('overwrite', False)

        if paths is None:
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

        if target is None:
            self.json({
                'error': True,
                'message': 'no target provided'
            })
            self.finish()
            return

        action = self.get_action(name=FM.Actions.COPY_FILES, module=session.get('type'), paths=paths, session=session,
                                 target=target, overwrite=overwrite)
        answer = action.run()

        self.json(answer)
        self.finish()
