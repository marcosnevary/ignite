from datetime import UTC, datetime

from src.database import load_data, save_data
from src.utils.clear_terminal import clear_terminal
from src.utils.options import list_goals, list_status, list_steps


def create_step() -> None:
    clear_terminal()
    data = load_data()
    goals = data["goals"]
    steps = data["steps"]
    status = data["status"]

    if not goals:
        print("No goals to step.")
        _ = input("Press enter to continue...")
        return

    list_goals()

    idx_goal = int(input("Select the goal to step (number): ")) - 1
    if not (0 <= idx_goal < len(goals)):
        print("Invalid goal number.")
        _ = input("Press enter to continue...")
        return

    list_status()

    idx_status = int(input("Select the status of the goal (number): ")) - 1
    if not (0 <= idx_status < len(status)):
        print("Invalid status number.")
        _ = input("Press enter to continue...")
        return

    steps.append(
        {
            "date": datetime.now(UTC).strftime("%d-%m-%Y"),
            "name": goals[idx_goal].lower().strip(),
            "status": status[idx_status],
        },
    )
    save_data()


def remove_step() -> None:
    clear_terminal()
    data = load_data()
    steps = data["steps"]

    if not steps:
        print("No steps to remove.")
        _ = input("Press enter to continue...")
        return

    list_steps()
    idx_step = int(input("Select the step to remove (number): ")) - 1
    if not (0 <= idx_step < len(steps)):
        print("Invalid step number.")
        _ = input("Press enter to continue...")
        return

    del steps[idx_step]
    save_data()


def edit_step() -> None:
    clear_terminal()
    data = load_data()
    goals = data["goals"]
    steps = data["steps"]
    status = data["status"]

    if not steps:
        print("No steps to edit.")
        _ = input("Press enter to continue...")
        return

    list_steps()
    idx_step = int(input("Select the step to edit (number): ")) - 1
    if not (0 <= idx_step < len(steps)):
        print("Invalid step number.")
        _ = input("Press enter to continue...")
        return

    list_goals()
    idx_goal = int(input("Select the new goal for the step (number): "))
    if not (0 <= idx_goal < len(goals)):
        print("Invalid goal number.")
        _ = input("Press enter to continue...")
        return

    list_status()
    idx_status = int(input("Select the new status for the step (number): "))
    if not (0 <= idx_status < len(status)):
        print("Invalid status number.")
        _ = input("Press enter to continue...")
        return

    steps[idx_step] = {
        "date": steps[idx_step]["date"],
        "name": goals[idx_goal].lower().strip(),
        "status": status[idx_status],
    }
    save_data()


def show_steps() -> None:
    clear_terminal()
    data = load_data()
    steps = data["steps"]

    if not steps:
        print("No steps found.")
        _ = input("Press enter to continue...")
        return

    list_steps()
    _ = input("Press enter to continue...")
