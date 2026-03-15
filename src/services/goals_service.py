from src.database import load_data, save_data
from src.utils.clear_terminal import clear_terminal
from src.utils.options import list_goals


def create_goal() -> None:
    clear_terminal()
    data = load_data()
    goals = data["goals"]

    if goals:
        list_goals()
    name = input("Enter the name of the new goal: ").lower().strip()
    if not name:
        print("goal name cannot be empty.")
        _ = input("Press enter to continue...")
        return

    goals.append(name)
    save_data()


def remove_goal() -> None:
    clear_terminal()
    data = load_data()
    goals = data["goals"]

    if not goals:
        print("No goals to remove.")
        _ = input("Press enter to continue...")
        return

    list_goals()
    idx_goal = int(input("Select the goal to remove (number): ")) - 1
    if not (0 <= idx_goal < len(goals)):
        print("Invalid goal number.")
        _ = input("Press enter to continue...")
        return

    del goals[idx_goal]
    save_data()


def edit_goal() -> None:
    clear_terminal()
    data = load_data()
    goals = data["goals"]

    if not goals:
        print("No goals to edit.")
        _ = input("Press enter to continue...")
        return

    list_goals()
    idx_goal = int(input("Select the goal to edit (number): ")) - 1
    if not (0 <= idx_goal < len(goals)):
        print("Invalid goal number.")
        _ = input("Press enter to continue...")
        return

    name = input("Enter the new name for the goal: ").lower().strip()
    goals[idx_goal] = name.lower().strip()
    save_data()


def show_goals() -> None:
    clear_terminal()
    data = load_data()
    goals = data["goals"]

    if not goals:
        print("No goals found.")
        _ = input("Press enter to continue...")
        return

    list_goals()
    _ = input("Press enter to continue...")
