from flask.helpers import get_debug_flag

from conduit.app import create_app
from conduit.settings import DevConfig, TestConfig

CONFIG = DevConfig if get_debug_flag() else TestConfig

app = create_app(CONFIG)
