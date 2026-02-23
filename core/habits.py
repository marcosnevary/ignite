from core.repository import load_data, save_data
from core.utils import clear_terminal, get_user_input, show_options


def create_habit(name):
    data = load_data()
    data["habits"].append(name.lower().strip())
    save_data()


def remove_habit(idx_habit):
    data = load_data()
    del data["habits"][idx_habit]
    save_data()


def edit_habit(idx_habit, name):
    data = load_data()
    data["habits"][idx_habit] = name
    save_data()


def habits():
    clear_terminal()
    data = load_data()
    habits = data["habits"]
    habits_functions = data["habits_functions"]
    idx_option = get_user_input(habits_functions, msg="Select an option: ")

    clear_terminal()
    if idx_option == 0:
        show_options(habits, title="Your habits:", format="itemize")
        print("=" * 64)
        new_habit_name = input("Enter the name of the new habit: ")
        create_habit(new_habit_name)

    if idx_option == 1:
        idx_habit = get_user_input(habits, msg="Select the habit to edit: ")
        new_habit_name = input("Enter the new name of the habit: ")
        edit_habit(idx_habit, new_habit_name)

    if idx_option == 2:
        idx_habit = get_user_input(habits, msg="Select the habit to remove: ")
        remove_habit(idx_habit)

    if idx_option == 3:
        show_options(habits, title="Your habits:", format="itemize")
        print("=" * 64)
        _ = input("Press enter to continue...")
