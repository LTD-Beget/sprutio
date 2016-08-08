from tornado import web
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch

from core import FM


class WebDavUpdateConnectionHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def post(self):

        params = self.get_post('params')

        if params is None:
            self.json({
                'error': True,
                'message': 'no params provided'
            })
            self.finish()
            return

        action = self.get_action(name=FM.Actions.WEBDAV_UPDATE, params=params)
        answer = action.run()

        self.json(answer)
        self.finish()

