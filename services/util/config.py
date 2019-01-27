import os
import yaml


class Config(object):
    _default_config = {
        "mqtt_host": "mustang.local",
        "mqtt_port": 1883,
        "t_charging": True,
        "t_max_cell_v": 2.65
    }

    def __init__(self, config_file_name="config.yml"):
        file_path = os.path.dirname(os.path.realpath(__file__))
        self._config_path = file_path.replace("services/util", config_file_name)
        self._config = self._default_config
        self._config.update(self._yaml_config())
        self._config_to_object()

    def update(self, key, value):
        if not key:
            return

        self._config[key] = value
        self._config_to_yaml()
        self._config_to_object()

    def delete_key(self, key):
        self._config.pop(key, None)
        self._config_to_yaml()
        try:
            delattr(self, key)
        except AttributeError as exc:
            print(f"Attr {key} not found. Skipped.")

    def _сonfig_to_yaml(self):
        with open(self._config_path, 'w+') as stream:
            try:
                yaml.dump(self._config, stream, default_flow_style=False)
            except yaml.YAMLError as exc:
                print(exc)

    def _config_to_object(self):
        for a, b in self._config.items():
            if isinstance(b, (list, tuple)):
                setattr(self, a,
                        [obj(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, obj(b) if isinstance(b, dict) else b)

    def _yaml_config(self):
        yaml_config = {}

        try:
            with open(self._config_path, 'r') as stream:
                try:
                    yaml_config = yaml.load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
        except FileNotFoundError as exc:
            print(exc)

        return yaml_config
