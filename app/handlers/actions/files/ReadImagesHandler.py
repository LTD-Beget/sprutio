from tornado import web

from core import FM
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch


class ReadImagesHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def post(self):

        paths = self.get_post('paths')
        session = self.get_post('session')

        if paths is None:
            self.json({
                'error': True,
                'message': 'no paths provided'
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

        action = self.get_action(name=FM.Actions.READ_IMAGES, module=session.get('type'), paths=paths, session=session)
        answer = action.run()

        self.json(answer)
        self.finish()
