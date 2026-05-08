import yaml


def load_config(config_path):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    required_keys = ["seed", "window", "version"]

    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing config key: {key}")

    return config