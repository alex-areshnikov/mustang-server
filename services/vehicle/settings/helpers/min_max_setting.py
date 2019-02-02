class MinMaxSetting:
    def __init__(self, min=0, max=10, step=1, initial_value=0):
        self._min = min
        self._max = max
        self._step = step
        self._value = initial_value

    @property
    def value(self):
        return self._value

    def increase(self):
        self._value += self._step
        self._adjust_value()
        if self._value > self._max:
            self._value = self._max

    def decrease(self):
        self._value -= self._step
        self._adjust_value()
        if self._value < self._min:
            self._value = self._min

    def _adjust_value(self):
        if isinstance(self._value, float):
            self._value = round(self._value, 2)
