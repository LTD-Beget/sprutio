import os
import sys

APP_PATH = os.path.dirname(os.path.dirname(__file__))
WEB_ROOT = os.path.join(APP_PATH, 'public')

app_modules = [
    os.path.join(APP_PATH, 'modules'),
    os.path.join(APP_PATH, 'classes')
]

sys.path = app_modules + sys.path

DEFAULT_COOKIE_TOKEN_NAME = 'token'
DEFAULT_LANGUAGE = 'ru'
DEFAULT_LOCALE = 'ru_RU'
DEFAULT_DATABASE = 'fm.db'
TRANSLATIONS_PATH = os.path.join(APP_PATH, "i18n")

LOCALES = {
    "ru": "ru_RU",
    "de": "de_DE",
    "en": "en_US"
}

LANGUAGES = ["ru", "en", "de"]

SETTINGS = {
    "preview_types": [
        "jpg",
        "jpeg",
        "png",
        "gif",
        "tif",
        "tiff"
    ],
    "preview_output": {
        "bgcolor": "#fff",
        "size": (128, 128),
        "format": "JPEG",
        "extension": ".jpg",
        "quality": 80
    },
    "block_size": 32768,
    "encodings": [
        "ascii",
        "big5",
        "euc-jp",
        "euc-kr",
        "gb2312",
        "hz-gb-2312",
        "ibm855",
        "ibm866",
        "iso-2022-jp",
        "iso-2022-kr",
        "iso-8859-2",
        "iso-8859-5",
        "iso-8859-7",
        "iso-8859-8",
        "koi8-r",
        "maccyrillic",
        "shift_jis",
        "tis-620",
        "utf-8",
        "utf-16le",
        "utf-16be",
        "utf-32le",
        "utf-32be",
        "windows-1250",
        "windows-1251",
        "windows-1252",
        "windows-1253",
        "windows-1255"
    ],
    "default_encoding": "utf-8",
    "path": APP_PATH,
    "cookie_secret": "943a702d06f34599aee1f8da8ef9f7296031d699",
    "template_path": WEB_ROOT,
    "preview_path": "/tmp/fm/preview",
    "login_url": "/login",
    "gzip": True,
    "debug": False
}
