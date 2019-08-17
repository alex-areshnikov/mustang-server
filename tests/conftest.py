import pytest
from unittest.mock import patch
from services.util.config import Config
from services.util.redis_storage import RedisStorage
from services.vehicle.lto.bank import Bank
from services.vehicle.lto.blank_bank import BlankBank
from services.vehicle.screen import Screen
from services.vehicle.lto.overcharge_processor import OverchargeProcessor
from services.vehicle.amplifier.clipping_processor import ClippingProcessor


@pytest.fixture
def config():
    return Config(storage=RedisStorage(db=1, erase_data=True))


@pytest.fixture
def make_config():
    def _make_config():
        return Config(storage=RedisStorage(db=1))

    yield _make_config


@pytest.fixture
def screen(config):
    return Screen(config, debug=True)


@pytest.fixture
def overcharge_processor():
    return OverchargeProcessor()


@pytest.fixture
def clipping_processor():
    return ClippingProcessor()


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
