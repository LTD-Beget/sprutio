import os

TYPE_FCGI = 'fcgi'
TYPE_MSGPACK = 'msgpack'

DEFAULT_RPC_HOST = os.getenv("FM_APP_DEFAULT_RPC_HOST", 'fm-rpc')
DEFAULT_RPC_PORT = os.getenv("FM_APP_DEFAULT_RPC_PORT", 8400)

# todo: сделать доступ как через ['это'], так и черезе точку.
servers = {
    # используется по умолнчаению
    # todo: сделать слияние конфигов. Сначала берем default, а поверх накладываем конфиг сервера если такой есть
    "default": {
        "type": TYPE_MSGPACK,
        "host": DEFAULT_RPC_HOST,
        "port": DEFAULT_RPC_PORT
    }
}
