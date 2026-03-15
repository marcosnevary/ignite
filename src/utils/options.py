from datetime import UTC, datetime

from rich import box
from rich.console import Console
from rich.table import Table

from src.database import load_data
from src.utils.common import days

console = Console()


def list_goals() -> None:
    data = load_data()
    goals = data["goals"]

    table = Table(
        box=box.HORIZONTALS,
        show_header=True,
        header_style="bold bright_red",
    )

    table.add_column("Option", style="bright_yellow", width=8)
    table.add_column("Goal", style="white", width=56)
    for idx, goal in enumerate(goals):
        table.add_row(f"{idx + 1}", f"{goal.replace('_', ' ').title()}")
    console.print(table)


def list_steps() -> None:
    data = load_data()
    steps = data["steps"]

    table = Table(
        box=box.HORIZONTALS,
        show_header=True,
        header_style="bold bright_red",
    )

    table.add_column("Option", style="bright_yellow", width=8)
    table.add_column("Goal", style="white", width=10)
    table.add_column("Description", style="white", width=42)
    table.add_column("Status", style="white", width=36)

    day_name = datetime.now(UTC).strftime("%A")

    for i, step in enumerate(steps):
        if day_name in step["days"]:
            table.add_row(
                f"{i + 1}",
                f"{step['goal'].replace('_', ' ').title()}",
                f"{step['description']}",
                f"{step['status'].replace('_', ' ').title()}",
            )
    console.print(table)


def list_status() -> None:
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


def days_menu() -> str:
    table = Table(
        box=box.HORIZONTALS,
        show_header=True,
        header_style="bold bright_red",
    )

    table.add_column("Option", style="bright_yellow", width=8)
    table.add_column("Day", style="white", width=56)

    for idx, day in days.items():
        table.add_row(f"{idx}", f"{day}")
    console.print(table)

    return input("Enter the number of the days (separated by commas): ")


def timer_settings_menu() -> int:
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
            f"{idx + 1}",
            f"{setting.replace('_', ' ').title()}",
            f"{value} minutes",
        )
    console.print(table)

    return int(input("Enter the number of the setting you want to change: "))


def main_menu() -> int:
    table = Table(
        box=box.HORIZONTALS,
        show_header=True,
        header_style="bold bright_red",
    )

    table.add_column("Option", style="bright_yellow", width=8)
    table.add_column("Description", style="white", width=56)

    options = {
        "1": "Goals",
        "2": "Steps",
        "3": "Pomodoro Timer",
        "4": "Statistics",
        "0": "Exit",
    }

    for option, description in options.items():
        table.add_row(option, description)
    console.print(table)
    return int(input("Enter the number of the option you want to select: "))


def goals_menu() -> int:
    table = Table(
        box=box.HORIZONTALS,
        show_header=True,
        header_style="bold bright_red",
    )

    table.add_column("Option", style="bright_yellow", width=8)
    table.add_column("Description", style="white", width=56)

    options = {
        "1": "Create a new goal",
        "2": "Edit an existing goal",
        "3": "Remove an existing goal",
        "4": "Show all goals",
        "0": "Return to main menu",
    }

    for option, description in options.items():
        table.add_row(option, description)
    console.print(table)
    return int(input("Enter the number of the option you want to select: "))


def steps_menu() -> int:
    table = Table(
        box=box.HORIZONTALS,
        show_header=True,
        header_style="bold bright_red",
    )

    table.add_column("Option", style="bright_yellow", width=8)
    table.add_column("Description", style="white", width=56)

    options = {
        "1": "Create a new step",
        "2": "Edit an existing step",
        "3": "Remove an existing step",
        "4": "Show all steps",
        "0": "Return to main menu",
    }

    for option, description in options.items():
        table.add_row(option, description)
    console.print(table)
    return int(input("Enter the number of the option you want to select: "))


def timer_menu() -> int:
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
