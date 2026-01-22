import os

class ConfigError(Exception):
    pass


def load_config(required_keys, defaults=None):
    config = {}
    defaults = defaults or {}

    for key in required_keys:
        value = os.getenv(key, defaults.get(key))
        if value is None:
            raise ConfigError(f"Missing required config: {key}")
        config[key] = value

    return config
