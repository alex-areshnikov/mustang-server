import pytest
from unittest.mock import patch
from services.util.config import Config


@pytest.fixture
def config(scope="function"):
    with patch.object(Config, '_сonfig_to_yaml'):
        with patch.object(Config, '_yaml_config', return_value={}):
            config = Config()
            yield config
            del config
