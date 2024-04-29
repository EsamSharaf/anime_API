from flask.helpers import get_debug_flag

from anime.app import create_app
from anime.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)
