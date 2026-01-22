import os
import pytest
from src.config_loader import load_config, ConfigError


def test_load_config_with_defaults():
    os.environ.pop("DB_HOST", None)
    config = load_config(["DB_HOST"], defaults={"DB_HOST": "localhost"})
    assert config["DB_HOST"] == "localhost"


def test_missing_required_config():
    os.environ.pop("DB_USER", None)
    try:
        load_config(["DB_USER"])
        assert False
    except ConfigError:
        assert True
