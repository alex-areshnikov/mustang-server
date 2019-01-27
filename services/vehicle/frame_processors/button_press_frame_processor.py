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

        self._button_resolver_methods = {
            self.CHARGING_INCREASE_BUTTON_ID: self._charging_increase,
            self.CHARGING_DECREASE_BUTTON_ID: self._charging_decrease,
            self.MAX_CELL_V_INCREASE_BUTTON_ID: self._max_cell_v_increase,
            self.MAX_CELL_V_DECREASE_BUTTON_ID: self._max_cell_v_decrease,
            self.BRIGHTNESS_INCREASE_BUTTON_ID: self._brightness_increase,
            self.BRIGHTNESS_DECREASE_BUTTON_ID: self._brightness_decrease
        }

    def process(self):
        self._button_resolver_methods.get(self._button_id, self._unknown_button_id)()

    def _charging_increase(self):
        print("Pressed: charging increase")

    def _charging_decrease(self):
        print("Pressed: charging decrease")

    def _max_cell_v_increase(self):
        print("Pressed: max_cell_v increase")

    def _max_cell_v_decrease(self):
        print("Pressed: max_cell_v decrease")

    def _brightness_increase(self):
        print("Pressed: brightness increase")

    def _brightness_decrease(self):
        print("Pressed: brightness decrease")

    def _unknown_button_id(self):
        print("Pressed: unknown button id")
