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

        if "error" in results and results['error']:
            self.set_status(500)
            self.application.logger.error('Error download file. %s' % pprint.pformat(results))
            self.write('Error download file.' + str(results.get("message")))
            self.finish()
            return

        if 'errors' in results.keys():
            errors = results["errors"]
        else:
            errors = ''
        results = results['data']

        if len(errors) > 0:
            self.set_status(500)

            self.write('Error download file.: <br/>')

            for f in errors:
                self.write(f + '<br/>')
            self.finish()
            return
        else:
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
