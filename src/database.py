import json
from pathlib import Path

_data = None


def load_data() -> dict:
    global _data
    if _data is None:
        with Path.open("data/data.json") as f:
            _data = json.load(f)
    return _data


def save_data() -> None:
    with Path.open("data/data.json", "w") as f:
        json.dump(_data, f, indent=4)
