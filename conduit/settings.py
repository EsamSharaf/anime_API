class Config(object):
    """Base configuration."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    # DB_NAME = 'dev.db'
    # Put the db file in project root
    # DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = "sqlite:///animeDB"
    # CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    # JWT_ACCESS_TOKEN_EXPIRES = timedelta(10 ** 6)


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///animeDB_test.db"
    # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    # BCRYPT_LOG_ROUNDS = 4
