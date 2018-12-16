import os
import yaml


class Config(object):
    _default_config = {
        "mqtt_host": "mustang.local",
        "mqtt_port": 1883
    }

    def __init__(self):
        self._config = self._default_config
        self._config.update(self._yaml_config())
        self._config_to_object()

    def _config_to_object(self):
        for a, b in self._config.items():
            if isinstance(b, (list, tuple)):
                setattr(self, a,
                        [obj(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, obj(b) if isinstance(b, dict) else b)

    def _yaml_config(self):
        yaml_config = {}
        file_path = os.path.dirname(os.path.realpath(__file__))
        config_path = file_path.replace("services/util", "config.yaml")

        try:
            with open(config_path, 'r') as stream:
                try:
                    yaml_config = yaml.load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
        except FileNotFoundError as exc:
            print(exc)

        return yaml_config
