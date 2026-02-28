from rich import box
from rich.console import Console
from rich.table import Table

from src.database import load_data

console = Console()


def list_habits():
    data = load_data()
    habits = data["habits"]

    table = Table(
        box=box.HORIZONTALS,
        show_header=True,
        header_style="bold bright_red",
    )

    table.add_column("Option", style="bright_yellow", width=8)
    table.add_column("Habit", style="white", width=56)
    for idx, habit in enumerate(habits):
        table.add_row(f"{idx + 1}", f"{habit.replace('_', ' ').title()}")
    console.print(table)


def list_records():
    data = load_data()
    records = data["records"]

    table = Table(
        box=box.HORIZONTALS,
        show_header=True,
        header_style="bold bright_red",
    )

    table.add_column("Option", style="bright_yellow", width=8)
    table.add_column("Date", style="white", width=10)
    table.add_column("Habit", style="white", width=10)
    table.add_column("Status", style="white", width=36)

    for i, record in enumerate(records):
        table.add_row(
            f"{i + 1}",
            f"{record['date']}",
            f"{record['name'].replace('_', ' ').title()}",
            f"{record['status'].replace('_', ' ').title()}",
        )
    console.print(table)


def list_status():
    data = load_data()
    status = data["status"]

    table = Table(
        box=box.HORIZONTALS,
        show_header=True,
        header_style="bold bright_red",
    )

    table.add_column("Option", style="bright_yellow", width=8)
    table.add_column("Status", style="white", width=56)

    for idx, stat in enumerate(status):
        table.add_row(f"{idx + 1}", f"{stat.replace('_', ' ').title()}")
    console.print(table)


def list_stats(habit):
    data = load_data()
    stats = data["habits_stats"][habit]

    table = Table(
        box=box.HORIZONTALS,
        show_header=True,
        header_style="bold bright_red",
    )

    table.add_column("Stat", style="white", width=32)
    table.add_column("Value", style="white", width=32)

    for idx, (stat, value) in enumerate(stats.items()):
        table.add_row(f"{stat.replace('_', ' ').title()}", f"{value}")
    console.print(table)


def timer_settings_menu():
    data = load_data()
    timer_settings = data["timer_settings"]

    table = Table(
        box=box.HORIZONTALS,
        show_header=True,
        header_style="bold bright_red",
    )

    table.add_column("ID", style="bright_yellow", width=2)
    table.add_column("Setting", style="white", width=32)
    table.add_column("Value", style="white", width=32)

    for idx, (setting, value) in enumerate(timer_settings.items()):
        table.add_row(
            f"{idx + 1}", f"{setting.replace('_', ' ').title()}", f"{value} minutes"
        )
    console.print(table)

    return int(input("Enter the number of the setting you want to change: "))


def main_menu():
    table = Table(
        box=box.HORIZONTALS,
        show_header=True,
        header_style="bold bright_red",
    )

    table.add_column("Option", style="bright_yellow", width=8)
    table.add_column("Description", style="white", width=56)

    options = {
        "1": "Habits",
        "2": "Records",
        "3": "Pomodoro Timer",
        "4": "Statistics",
        "0": "Exit",
    }

    for option, description in options.items():
        table.add_row(option, description)
    console.print(table)
    return int(input("Enter the number of the option you want to select: "))


def habits_menu():
    table = Table(
        box=box.HORIZONTALS,
        show_header=True,
        header_style="bold bright_red",
    )

    table.add_column("Option", style="bright_yellow", width=8)
    table.add_column("Description", style="white", width=56)

    options = {
        "1": "Create a new habit",
        "2": "Edit an existing habit",
        "3": "Remove an existing habit",
        "4": "Show all habits",
        "0": "Return to main menu",
    }

    for option, description in options.items():
        table.add_row(option, description)
    console.print(table)
    return int(input("Enter the number of the option you want to select: "))


def records_menu():
    table = Table(
        box=box.HORIZONTALS,
        show_header=True,
        header_style="bold bright_red",
    )

    table.add_column("Option", style="bright_yellow", width=8)
    table.add_column("Description", style="white", width=56)

    options = {
        "1": "Create a new record",
        "2": "Edit an existing record",
        "3": "Remove an existing record",
        "4": "Show all records",
        "0": "Return to main menu",
    }

    for option, description in options.items():
        table.add_row(option, description)
    console.print(table)
    return int(input("Enter the number of the option you want to select: "))


def timer_menu():
    table = Table(
        box=box.HORIZONTALS,
        show_header=True,
        header_style="bold bright_red",
    )

    table.add_column("Option", style="bright_yellow", width=8)
    table.add_column("Description", style="white", width=56)

    options = {
        "1": "Configure timer settings",
        "2": "Start timer",
        "0": "Return to main menu",
    }

    for option, description in options.items():
        table.add_row(option, description)
    console.print(table)
    return int(input("Enter the number of the option you want to select: "))
