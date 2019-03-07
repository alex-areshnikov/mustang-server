from services.util.redis_storage import RedisStorage

import os
import sys
import yaml


class Config:
    MQTT_HOST = "mqtt_host"
    MQTT_PORT = "mqtt_port"
    SCREEN_SETTING_CHARGING = "screen_setting_charging"
    SCREEN_SETTING_MAX_CELL_V = "screen_setting_max_cell_v"
    SCREEN_SETTING_BRIGHTNESS = "screen_setting_brightness"
    SCREEN_SETTING_TRUNK_LIGHTS = "screen_setting_trunk_lights"

    CONFIG_KEYS = [
        MQTT_HOST,
        MQTT_PORT,
        SCREEN_SETTING_CHARGING,
        SCREEN_SETTING_MAX_CELL_V,
        SCREEN_SETTING_BRIGHTNESS,
        SCREEN_SETTING_TRUNK_LIGHTS
    ]

    DEFAULT_CONFIG = {
        MQTT_HOST: "mustang.local",
        MQTT_PORT: 1883,
        SCREEN_SETTING_CHARGING: "ON",
        SCREEN_SETTING_MAX_CELL_V: 2.65,
        SCREEN_SETTING_BRIGHTNESS: 10,
        SCREEN_SETTING_TRUNK_LIGHTS: "OFF"
    }

    CONFIG_TYPE_CONVERTERS = {
        MQTT_HOST: lambda value: value.decode("utf-8"),
        MQTT_PORT: lambda value: int(value),
        SCREEN_SETTING_CHARGING: lambda value: value.decode("utf-8"),
        SCREEN_SETTING_MAX_CELL_V: lambda value: float(value),
        SCREEN_SETTING_BRIGHTNESS: lambda value: int(value),
        SCREEN_SETTING_TRUNK_LIGHTS: lambda value: value.decode("utf-8")
    }

    def __init__(self, storage=RedisStorage()):
        self._storage = storage

    def __getattr__(self, method_name):
        if method_name in self.CONFIG_KEYS:
            return self._get(method_name)
        else:
            raise AttributeError(f'No such attribute: {method_name}')

    def _get(self, config_key):
        converter = self.CONFIG_TYPE_CONVERTERS.get(config_key)
        value = self._storage.get(config_key)
        return converter(value) if value else self.DEFAULT_CONFIG.get(config_key)

    def update(self, key, value):
        self._storage.set(key, value)
