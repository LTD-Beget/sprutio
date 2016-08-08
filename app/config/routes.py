from handlers.actions.main import RestoreSessionHandler
from handlers.actions.main import SaveSessionHandler
from handlers.actions.main import InitSessionHandler
from handlers.actions.main import CheckStatusHandler
from handlers.actions.main import CancelOperationHandler
from handlers.actions.main import LoadSettingsHandler
from handlers.actions.main import SaveSettingsHandler
# from handlers.actions.main import LogoutHandler
from handlers.actions.files import ListFilesHandler
from handlers.actions.files import RemoveFilesHandler
from handlers.actions.files import ChmodFilesHandler
from handlers.actions.files import MakeDirHandler
from handlers.actions.files import NewFileHandler
from handlers.actions.files import ReadFileHandler
from handlers.actions.files import ReadImagesHandler
from handlers.actions.files import WriteFileHandler
from handlers.actions.files import RenameFileHandler
from handlers.actions.files import AnalyzeSizeHandler
from handlers.actions.files import CreateCopyHandler
from handlers.actions.files import CopyFilesHandler
from handlers.actions.files import MoveFilesHandler
from handlers.actions.files import DownloadHandler
from handlers.actions.find import FindFilesHandler
from handlers.actions.archive import ArchiveCreateHandler
from handlers.actions.archive import ArchiveExtractHandler
from handlers.actions.find import FindTextHandler
from handlers.actions.home import InitCallbackHandler

from handlers.actions.htaccess import ReadRulesHandler
from handlers.actions.htaccess import SaveRulesHandler

from handlers.actions.ftp import FtpCreateConnectionHandler
from handlers.actions.ftp import FtpUpdateConnectionHandler
from handlers.actions.ftp import FtpRemoveConnectionHandler

from handlers.actions.sftp import SftpCreateConnectionHandler
from handlers.actions.sftp import SftpUpdateConnectionHandler
from handlers.actions.sftp import SftpRemoveConnectionHandler

from handlers.actions.webdav import WebDavCreateConnectionHandler
from handlers.actions.webdav import WebDavUpdateConnectionHandler
from handlers.actions.webdav import WebDavRemoveConnectionHandler

from handlers import MainHandler
from handlers import UploadHandler
from handlers import AuthHandler
from handlers import LoginHandler
from handlers import LogoutHandler

HANDLERS = [
    (r"/", MainHandler.MainHandler),
    (r"/auth", AuthHandler.AuthHandler),
    (r"/login", LoginHandler.LoginHandler),
    (r"/logout", LogoutHandler.LogoutHandler),
    (r"/upload", UploadHandler.UploadHandler),
    (r"/actions/home/init_callback", InitCallbackHandler.InitCallbackHandler),
    (r"/actions/main/load_settings", LoadSettingsHandler.LoadSettingsHandler),
    (r"/actions/main/restore_session", RestoreSessionHandler.RestoreSessionHandler),
    (r"/actions/main/save_session", SaveSessionHandler.SaveSessionHandler),
    (r"/actions/main/init_session", InitSessionHandler.InitSessionHandler),
    (r"/actions/main/check_status", CheckStatusHandler.CheckStatusHandler),
    (r"/actions/main/cancel_operation", CancelOperationHandler.CancelOperationHandler),
    (r"/actions/main/save_settings", SaveSettingsHandler.SaveSettingsHandler),
    (r"/actions/main/logout", LogoutHandler.LogoutHandler),
    (r"/actions/files/list", ListFilesHandler.ListFilesHandler),
    (r"/actions/files/remove", RemoveFilesHandler.RemoveFilesHandler),
    (r"/actions/files/chmod", ChmodFilesHandler.ChmodFilesHandler),
    (r"/actions/files/mkdir", MakeDirHandler.MakeDirHandler),
    (r"/actions/files/newfile", NewFileHandler.NewFileHandler),
    (r"/actions/files/rename", RenameFileHandler.RenameFileHandler),
    (r"/actions/files/read", ReadFileHandler.ReadFileHandler),
    (r"/actions/files/read_images", ReadImagesHandler.ReadImagesHandler),
    (r"/actions/files/write", WriteFileHandler.WriteFileHandler),
    (r"/actions/files/analyze_size", AnalyzeSizeHandler.AnalyzeSizeHandler),
    (r"/actions/files/create_copy", CreateCopyHandler.CreateCopyHandler),
    (r"/actions/files/copy", CopyFilesHandler.CopyFilesHandler),
    (r"/actions/files/move", MoveFilesHandler.MoveFilesHandler),
    (r"/actions/files/download", DownloadHandler.DownloadHandler),
    (r"/actions/find/files", FindFilesHandler.FindFilesHandler),
    (r"/actions/find/text", FindTextHandler.FindTextHandler),
    (r"/actions/htaccess/read_rules", ReadRulesHandler.ReadRulesHandler),
    (r"/actions/htaccess/save_rules", SaveRulesHandler.SaveRulesHandler),
    (r"/actions/archive/create", ArchiveCreateHandler.ArchiveCreateHandler),
    (r"/actions/archive/extract", ArchiveExtractHandler.ArchiveExtractHandler),
    (r"/actions/ftp/create", FtpCreateConnectionHandler.FtpCreateConnectionHandler),
    (r"/actions/ftp/update", FtpUpdateConnectionHandler.FtpUpdateConnectionHandler),
    (r"/actions/ftp/remove", FtpRemoveConnectionHandler.FtpRemoveConnectionHandler),
    (r"/actions/sftp/create", SftpCreateConnectionHandler.SftpCreateConnectionHandler),
    (r"/actions/sftp/update", SftpUpdateConnectionHandler.SftpUpdateConnectionHandler),
    (r"/actions/sftp/remove", SftpRemoveConnectionHandler.SftpRemoveConnectionHandler),
    (r"/actions/webdav/create", WebDavCreateConnectionHandler.WebDavCreateConnectionHandler),
    (r"/actions/webdav/update", WebDavUpdateConnectionHandler.WebDavUpdateConnectionHandler),
    (r"/actions/webdav/remove", WebDavRemoveConnectionHandler.WebDavRemoveConnectionHandler)
]
