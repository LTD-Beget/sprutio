import json
from tornado import web
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch
from core import FM
from email import utils
import pprint


class DownloadHandler(BaseHandler):

    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def post(self):

        session = json.loads(self.get_argument("session"))
        paths = json.loads(self.get_argument("paths"))
        mode = self.get_argument("mode")

        action = self.get_action(name=FM.Actions.DOWNLOAD, module=session.get('type'), paths=paths, session=session,
                                 mode=mode)
        results = action.run()

        # handle global error during RPC request
        if 'error' in results and results['error']:
            self.application.logger.error('Error downloading file: {}'.format(pprint.pformat(results)))
            self.set_status(500)

            self.write('Error downloading file: {}'.format(results.get('message')))

            self.finish()
            return

        # handle errors for some files during request
        if 'errors' in results and results['errors']:
            self.set_status(500)

            self.write('Error downloading the following files: <br/>')
            for f in results['errors']:
                self.write(f + '<br/>')

            self.finish()
            return

        download_path = results["download_path"]
        filename = results["file_name"]

        mtime = results["mtime"]
        inode = results["inode"]
        size = results["size"]

        self.set_header("X-Accel-Redirect", download_path)
        self.set_header("Content-Type", "application/octet-stream")
        self.set_header("Last-Modified", utils.formatdate(mtime))
        self.set_header("ETag", "%x-%x-%x" % (inode, size, mtime))
        self.set_header("Connection", "close")
        self.set_header("Content-Disposition", "attachment; filename=\"%s\"" % filename)

        self.write('')
        self.finish()
