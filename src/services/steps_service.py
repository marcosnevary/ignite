from src.database import load_data, save_data
from src.utils.clear_terminal import clear_terminal
from src.utils.common import days
from src.utils.options import days_menu, list_goals, list_status, list_steps


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

    idx_goal = int(input("Select the goal for the step (number): ")) - 1
    if not (0 <= idx_goal < len(goals)):
        print("Invalid goal number.")
        _ = input("Press enter to continue...")
        return

    step_description = input("Enter the description of the step: ")

    active_days = days_menu()
    active_days = active_days.replace(",", "")
    active_days = active_days.replace(" ", "")
    print(active_days)
    if not all(day.strip().isdigit() and 1 <= int(day.strip()) <= 7 for day in active_days):  # noqa: PLR2004
        print("Invalid days input.")
        _ = input("Press enter to continue...")
        return
    active_days = [days[int(day.strip())] for day in active_days]

    steps.append(
        {
            "goal": goals[idx_goal].lower().strip(),
            "description": step_description,
            "status": status[1],
            "days": active_days,
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

    days = days_menu().strip().split(",")
    if not all(day.strip().isdigit() and 1 <= int(day.strip()) <= 7 for day in days):  # noqa: PLR2004
        print("Invalid days input.")
        _ = input("Press enter to continue...")
        return
    days = [int(day.strip()) for day in days]

    steps[idx_step] = {
        "description": steps[idx_step]["description"],
        "goal": goals[idx_goal].lower().strip(),
        "status": status[idx_status],
        "days": days,
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
