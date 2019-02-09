import os
import pytest
from unittest.mock import patch
from services.util.config import Config
from services.vehicle.lto.bank import Bank
from services.vehicle.lto.blank_bank import BlankBank
from services.vehicle.screen import Screen


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


@pytest.fixture
def screen(config):
    return Screen(config, debug=True)


@pytest.fixture
def bank():
    voltages = [2.3, 4.61, 6.93, 9.26, 11.6, 13.95]
    return Bank(bank_number=2, bank_voltages={"voltages": voltages})


@pytest.fixture
def blank_bank():
    return BlankBank(bank_number=2)


@pytest.fixture
def frame_callback():
    def _frame_callback(actions={}):
        pass

    return _frame_callback
