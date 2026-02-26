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

    table.add_column("ID", style="bright_yellow", justify="center", width=2)
    table.add_column("Habit", style="white", width=16)
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

    table.add_column("ID", style="bright_yellow", width=2)
    table.add_column("Date", style="white", width=10)
    table.add_column("Habit", style="white", width=10)
    table.add_column("Status", style="white", width=42)

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

    print("=" * 64)
    for idx, stat in enumerate(status):
        print(f"{idx + 1}. {stat.replace('_', ' ').title()}")
    print("=" * 64)


def list_streaks():
    data = load_data()
    streaks = data["max_streaks"]

    print("=" * 64)
    for habit, streak in streaks.items():
        print(f"{habit.title()}: {streak} days")
    print("=" * 64)


def main_menu():
    table = Table(
        box=box.HORIZONTALS,
        show_header=True,
        header_style="bold bright_red",
    )

    table.add_column("Option", style="bright_yellow", width=8)
    table.add_column("Description", style="white", width=56)

    options = {"1": "Habits", "2": "Records", "3": "Statistics", "0": "Exit"}

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


def statistics_menu():
    print("=" * 64)
    print("1. Show streaks")
    print("=" * 64)
    return int(input("Enter the number of the option you want to select: "))
