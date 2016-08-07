import beget_msgpack
from config import rpc


class BaseAction(object):
    @property
    def redis(self):
        return self.application.redis

    @staticmethod
    def get_rpc_request(user=None, password=None, logger=None):
        factory = beget_msgpack.RequestFactory(rpc, user=user, password=password, logger=logger)
        request = factory.get_request('default')
        return request

    @staticmethod
    def process_result(result):
        answer = {}

        if result.has_error():
            answer['error'] = True

            if result.has_method_errors():
                errors_list = []
                collection = result.get_method_error()
                for error_object in collection:
                    errors_list.append({
                        'type': error_object.get_type(),
                        'message': error_object.message,
                        'code': error_object.code
                    })

                answer['method_errors'] = errors_list

            if result.has_request_error():
                errors_list = []
                collection = result.get_request_error()
                for error_object in collection:
                    errors_list.append({
                        'type': error_object.get_type(),
                        'message': error_object.message,
                        'code': error_object.code
                    })

                answer['request_error'] = errors_list
        else:
            answer = result.get_method_result()

        return answer

    def __init__(self, request, **kwargs):
        self.application = request.application
        self.logger = request.application.logger
        self.request = request


class Modules(object):
    HOME = "home"
    FTP = "ftp"
    SFTP = "sftp"
    WEBDAV = "webdav"


class Actions(object):
    RESTORE_SESSION = "actions.main.restore_session.RestoreSession"
    SAVE_SESSION = "actions.main.save_session.SaveSession"
    INIT_SESSION = "actions.main.init_session.InitSession"
    INIT_CALLBACK = 'actions.main.init_callback.InitCallback'
    SHARE_ACCESS = 'actions.main.share_access.ShareAccess'
    CHECK_STATUS = "actions.main.check_status.CheckStatus"
    CANCEL_OPERATION = "actions.main.cancel_operation.CancelOperation"
    LOAD_SETTINGS = "actions.main.load_settings.LoadSettings"
    SAVE_SETTINGS = "actions.main.save_settings.SaveSettings"
    GET_CREDENTIALS = "actions.main.get_credentials.GetCredentials"
    LOGOUT = 'actions.main.logout.Logout'

    DOWNLOAD = 'actions.files.download.DownloadFiles'
    UPLOAD = 'actions.files.upload.UploadFile'
    LIST_FILES = 'actions.files.list.ListFiles'
    REMOVE_FILES = 'actions.files.remove.RemoveFiles'
    CHMOD_FILES = 'actions.files.chmod.ChmodFiles'
    MAKE_DIR = 'actions.files.mkdir.MakeDir'
    NEW_FILE = 'actions.files.newfile.NewFile'
    READ_FILE = 'actions.files.read.ReadFile'
    READ_IMAGES = 'actions.files.read_images.ReadImages'
    WRITE_FILE = 'actions.files.write.WriteFile'
    RENAME_FILE = 'actions.files.rename.RenameFile'
    ANALYZE_SIZE = 'actions.files.analyze_size.AnalyzeSize'

    COPY_FILES = 'actions.files.copy.CopyFiles'
    MOVE_FILES = 'actions.files.move.MoveFiles'
    CREATE_COPY = 'actions.files.create_copy.CreateCopy'

    FIND_FILES = 'actions.find.files.FindFiles'
    FIND_TEXT = 'actions.find.text.FindText'

    FTP_CREATE = 'actions.ftp.create.CreateFtp'
    FTP_UPDATE = 'actions.ftp.update.UpdateFtp'
    FTP_REMOVE = 'actions.ftp.remove.RemoveFtp'

    SFTP_CREATE = 'actions.sftp.create.CreateSftp'
    SFTP_UPDATE = 'actions.sftp.update.UpdateSftp'
    SFTP_REMOVE = 'actions.sftp.remove.RemoveSftp'

    WEBDAV_CREATE = 'actions.webdav.create.CreateWebDav'
    WEBDAV_UPDATE = 'actions.webdav.update.UpdateWebDav'
    WEBDAV_REMOVE = 'actions.webdav.remove.RemoveWebDav'

    CHECK_HTPASSWD = 'actions.htaccess.check_passwd.CheckPassword'
    SET_HTPASSWD = 'actions.htaccess.set_passwd.SetPassword'
    REMOVE_HTPASSWD = 'actions.htaccess.remove_passwd.RemovePassword'
    HTACCESS_READ_RULES = 'actions.htaccess.read_rules.ReadRules'
    HTACCESS_SAVE_RULES = 'actions.htaccess.save_rules.SaveRules'

    CREATE_ARCHIVE = 'actions.archive.create.CreateArchive'
    EXTRACT_ARCHIVE = 'actions.archive.extract.ExtractArchive'


# Aliases for FM actions
class Action(object):
    HOME = "FM.action.HomeFtp"
    REMOTE_FTP = "FM.action.RemoteFtp"
    SFTP = "FM.action.Sftp"
    REMOTE_WEBDAV = "FM.action.RemoteWebDav"
    LOCAL = 'FM.action.Local'
    SITE_LIST = 'FM.action.SiteList'

    REFRESH = 'FM.action.Refresh'
    UPLOAD = 'FM.action.Upload'

    OPEN_DIRECTORY = 'FM.action.Open'
    NAVIGATE = 'FM.action.Navigate'
    COPY_ENTRY = 'FM.action.CopyEntry'
    COPY_PATH = 'FM.action.CopyPath'

    UP = 'FM.action.Up'
    ROOT = 'FM.action.Root'

    VIEW = 'FM.action.View'
    EDIT = 'FM.action.Edit'
    CHMOD = 'FM.action.Chmod'
    COPY = 'FM.action.Copy'
    CREATE_COPY = 'FM.action.CreateCopy'
    MOVE = 'FM.action.Move'
    RENAME = 'FM.action.Rename'
    REMOVE = 'FM.action.Remove'

    NEW_FOLDER = 'FM.action.NewFolder'
    NEW_FILE = 'FM.action.NewFile'

    DOWNLOAD_BASIC = 'FM.action.DownloadBasic'
    DOWNLOAD_ARCHIVE = 'FM.action.DownloadArchive'
    DOWNLOAD_ZIP = 'FM.action.DownloadZip'
    DOWNLOAD_BZ2 = 'FM.action.DownloadBZ2'
    DOWNLOAD_GZIP = 'FM.action.DownloadGZip'
    DOWNLOAD_TAR = 'FM.action.DownloadTar'

    HTPASSWD = 'FM.action.Htpasswd'
    IP_BLOCK = 'FM.action.IPBlock'
    SHARE_ACCESS = 'FM.action.ShareAccess'
    SETTINGS = 'FM.action.Settings'

    SEARCH_FILES = 'FM.action.SearchFiles'
    SEARCH_TEXT = 'FM.action.SearchText'
    ANALYZE_SIZE = 'FM.action.AnalyzeSize'

    FIND_FILES = 'FM.action.FindFiles'
    FIND_TEXT = 'FM.action.FindText'

    CREATE_ARCHIVE = 'FM.action.CreateArchive'
    EXTRACT_ARCHIVE = 'FM.action.ExtractArchive'

    HELP = 'FM.action.Help'
    LOGOUT = 'FM.action.Logout'


class ActionsProvider:
    @staticmethod
    def get_action(action_name, request, *args, **kwargs):
        module_name = ActionsProvider.get_module_name(action_name, *args, **kwargs)
        module_obj = __import__(module_name)

        # Find module by name
        action_class = None
        chunks = action_name.split('.')
        for chunk in chunks:
            action_class = getattr(module_obj, chunk)
            module_obj = getattr(module_obj, chunk)

        return action_class(request=request, *args, **kwargs)

    @staticmethod
    def get_module_name(action_name, module=Modules.HOME, *args, **kwargs):
        return '%s.%s' % (module, action_name.rsplit('.', 1)[0])
