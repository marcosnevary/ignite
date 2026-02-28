import time

from rich.progress import BarColumn, Progress, ProgressColumn, Task, TextColumn
from rich.text import Text

from src.database import load_data, save_data
from src.utils.clear_terminal import clear_terminal
from src.utils.options import timer_settings_menu


class RemainingTimeColumn(ProgressColumn):
    def render(self, task: Task):
        restante = task.total - task.completed
        horas = int(restante // 3600)
        minutos = int((restante % 3600) // 60)
        segundos = int(restante % 60)
        return Text(f"{horas:02d}:{minutos:02d}:{segundos:02d}", style="cyan")


def start_timer():
    clear_terminal()

    data = load_data()
    timer_settings = data["timer_settings"]
    break_minutes = timer_settings["break_duration"]
    pomodoro_minutes = timer_settings["pomodoro_duration"]

    break_seconds = break_minutes * 60
    pomodoro_seconds = pomodoro_minutes * 60

    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TextColumn("•"),
        RemainingTimeColumn(),
    ) as progress:
        task = progress.add_task("Pomodoro", total=pomodoro_seconds)

        for _ in range(int(pomodoro_seconds)):
            time.sleep(1)
            progress.update(task, advance=1)

    _ = input("Pomodoro session completed! Press enter to start the break...")

    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TextColumn("•"),
        RemainingTimeColumn(),
    ) as progress:
        task = progress.add_task("Break", total=break_seconds)

        for _ in range(int(break_seconds)):
            time.sleep(1)
            progress.update(task, advance=1)

    print("Break session completed!")
    option = input("Do you want to start another Pomodoro session? (y/n): ")
    if option.lower() == "y":
        start_timer()
    return


def configure_timer():
    clear_terminal()

    data = load_data()
    timer_settings = data["timer_settings"]

    idx_menu = timer_settings_menu()
    if idx_menu == 1:
        new_value = int(input("Enter the new value for the timer setting: "))
        timer_settings["pomodoro_duration"] = new_value
    elif idx_menu == 2:
        new_value = int(input("Enter the new value for the timer setting: "))
        timer_settings["break_duration"] = new_value

    save_data()
