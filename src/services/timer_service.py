import time

from src.database import load_data, save_data
from src.utils.clear_terminal import clear_terminal
from src.utils.options import timer_settings_menu


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


def start_timer():
    data = load_data()
    timer_settings = data["timer_settings"]

    break_minutes = timer_settings["break_duration"]
    pomodoro_minutes = timer_settings["pomodoro_duration"]

    for remaining_seconds in range(int(pomodoro_minutes * 60), 0, -1):
        minutes, seconds = divmod(remaining_seconds, 60)
        print(f"{minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)

    print("00:00")

    _ = input("Pomodoro session completed! Press enter to start the break...")

    for remaining_seconds in range(int(break_minutes * 60), 0, -1):
        minutes, seconds = divmod(remaining_seconds, 60)
        print(f"{minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)

    print("00:00")

    _ = input("Break session completed! Press enter to continue...")
