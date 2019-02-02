import os
import pytest
from unittest.mock import patch
from services.util.config import Config


@pytest.fixture
def config():
    with patch.object(Config, '_сonfig_to_yaml'):
        with patch.object(Config, '_yaml_config', return_value={}):
            config = Config()
            yield config
            del config


@pytest.fixture
def make_config():
    def _make_config():
        return Config(config_file_name="test_config.yaml")

    yield _make_config
    os.remove(Config(config_file_name="test_config.yaml").config_path)
