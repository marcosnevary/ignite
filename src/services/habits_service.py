from src.database import load_data, save_data
from src.utils.clear_terminal import clear_terminal
from src.utils.options import list_habits


def create_habit():
    clear_terminal()
    data = load_data()
    habits = data["habits"]

    list_habits()
    name = input("Enter the name of the new habit: ").lower().strip()
    if not name:
        print("Habit name cannot be empty.")
        _ = input("Press enter to continue...")
        return

    habits.append(name)
    save_data()


def remove_habit():
    clear_terminal()
    data = load_data()
    habits = data["habits"]

    if not habits:
        print("No habits to remove.")
        _ = input("Press enter to continue...")
        return

    list_habits()
    idx_habit = int(input("Select the habit to remove (number): ")) - 1
    if not (0 <= idx_habit < len(habits)):
        print("Invalid habit number.")
        _ = input("Press enter to continue...")
        return

    del habits[idx_habit]
    save_data()


def edit_habit():
    clear_terminal()
    data = load_data()
    habits = data["habits"]

    if not habits:
        print("No habits to edit.")
        _ = input("Press enter to continue...")
        return

    list_habits()
    idx_habit = int(input("Select the habit to edit (number): ")) - 1
    if not (0 <= idx_habit < len(habits)):
        print("Invalid habit number.")
        _ = input("Press enter to continue...")
        return

    name = input("Enter the new name for the habit: ").lower().strip()
    habits[idx_habit] = name.lower().strip()
    save_data()


def show_habits():
    clear_terminal()
    data = load_data()
    habits = data["habits"]

    if not habits:
        print("No habits found.")
        _ = input("Press enter to continue...")
        return

    list_habits()
    _ = input("Press enter to continue...")
