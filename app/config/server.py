import os

DEFAULT_PORT = os.getenv("FM_APP_DEFAULT_PORT", 8300)
DEFAULT_HOST = os.getenv("FM_APP_DEFAULT_HOST", '127.0.0.1')
DEBUG_MODE = os.getenv("FM_APP_DEBUG_MODE", False)

# Xheaders using behind proxy like nginx
# http://tornado.readthedocs.org/en/latest/guide/running.html?highlight=xheaders#running-behind-a-load-balancer
XHEADERS = True

# For uploading a big files (2Gb)
# Max buffer in bytes that can be read into memory at once
MAX_BUFFER_SIZE = 2147483648

# limit the amount of data read into memory at one time per request
CHUNK_SIZE = 1048576

# for slow operations
# allow time limits to be placed on the reading of requests.
IDLE_CONNECTION_TIMEOUT = 7200
BODY_TIMEOUT = 7200

# Cookie lifetime in days
COOKIE_EXPIRE = 1

# Redis settings
REDIS_DEFAULT_HOST = os.getenv("FM_REDIS_HOST", 'localhost')
REDIS_DEFAULT_PORT = int(os.getenv("FM_REDIS_PORT", 6379))
REDIS_DEFAULT_EXPIRE = int(os.getenv("FM_REDIS_EXPIRE", 86400))

# Sendfile settings
SENDFILE_DEFAULT_HOST = os.getenv("FM_APP_SENDFILE_HOST", 'localhost')
SENDFILE_DEFAULT_PORT = int(os.getenv("FM_APP_SENDFILE_PORT", 56100))
