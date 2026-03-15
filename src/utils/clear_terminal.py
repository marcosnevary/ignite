import os
import subprocess


def clear_terminal() -> None:
    command = ["cls"] if os.name == "nt" else ["clear"]
    subprocess.run(command, check=False)  # noqa: S603
