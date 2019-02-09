from services.vehicle.settings.charging_setting import ChargingSetting
from services.vehicle.settings.max_cell_voltage_setting import MaxCellVoltageSetting
from services.vehicle.settings.brightness_setting import BrightnessSetting
from services.vehicle.settings.unknown_setting import UnknownSetting


class ButtonPressFrameProcessor:
    BUTTON_ID_INDEX = 2
    BUTTON_PRESS_STATE_INDEX = 3

    CHARGING_INCREASE_BUTTON_ID = b'\x0A'
    CHARGING_DECREASE_BUTTON_ID = b'\x09'
    MAX_CELL_V_INCREASE_BUTTON_ID = b'\x06'
    MAX_CELL_V_DECREASE_BUTTON_ID = b'\x07'
    BRIGHTNESS_INCREASE_BUTTON_ID = b'\x0D'
    BRIGHTNESS_DECREASE_BUTTON_ID = b'\x0C'

    def __init__(self, frame):
        self._button_id = bytes([frame[self.BUTTON_ID_INDEX]])
        self._press_state = bytes([frame[self.BUTTON_PRESS_STATE_INDEX]])

        self._buttons_processors = {
            self.CHARGING_INCREASE_BUTTON_ID: ChargingSetting,
            self.CHARGING_DECREASE_BUTTON_ID: ChargingSetting,
            self.MAX_CELL_V_INCREASE_BUTTON_ID: MaxCellVoltageSetting,
            self.MAX_CELL_V_DECREASE_BUTTON_ID: MaxCellVoltageSetting,
            self.BRIGHTNESS_INCREASE_BUTTON_ID: BrightnessSetting,
            self.BRIGHTNESS_DECREASE_BUTTON_ID: BrightnessSetting
        }

        self._increase_ids = [
            self.CHARGING_INCREASE_BUTTON_ID,
            self.MAX_CELL_V_INCREASE_BUTTON_ID,
            self.BRIGHTNESS_INCREASE_BUTTON_ID
        ]

        self._decrease_ids = [
            self.CHARGING_DECREASE_BUTTON_ID,
            self.MAX_CELL_V_DECREASE_BUTTON_ID,
            self.BRIGHTNESS_DECREASE_BUTTON_ID
        ]

    def process(self, callback):
        buttons_processor = self._buttons_processors.get(self._button_id, UnknownSetting)()

        if(self._button_id in self._increase_ids):
            buttons_processor.increase()

        if(self._button_id in self._decrease_ids):
            buttons_processor.decrease()

        callback({"settings_update": True})
