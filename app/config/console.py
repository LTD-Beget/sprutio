from tornado.options import define, options

from . import server, settings, rpc


def parse_options():
    define("host", default=server.DEFAULT_HOST, help="Server run on the given host", type=str)
    define("port", default=server.DEFAULT_PORT, help="Server run on the given port", type=int)
    define("rpc_host", default=rpc.DEFAULT_RPC_HOST, help="RPC Server run on the given host", type=str)
    define("rpc_port", default=rpc.DEFAULT_RPC_PORT, help="RPC Server run on the given port", type=int)

    define("debug", default=server.DEBUG_MODE, help="Debug mode")
    define("database", default=settings.DEFAULT_DATABASE, help="Debug mode")

    options.parse_command_line()
    return options

