import os
import pytest
from src.config_loader import load_config
from src.exceptions import ConfigError


def test_load_config_with_default():
    os.environ.pop("TEST_KEY", None)
    config = load_config(["TEST_KEY"], defaults={"TEST_KEY": "value"})
    assert config["TEST_KEY"] == "value"


def test_missing_required_key():
    os.environ.pop("MISSING_KEY", None)
    with pytest.raises(ConfigError):
        load_config(["MISSING_KEY"])
