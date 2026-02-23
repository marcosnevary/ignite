import json

_data = None


def load_data():
    global _data
    if _data is None:
        with open("data/data.json", "r") as f:
            _data = json.load(f)
    return _data


def save_data():
    global _data
    with open("data/data.json", "w") as f:
        json.dump(_data, f, indent=4)
