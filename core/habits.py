from core.repository import load_data
from core.utils import get_user_input, show_options


def create_habit(name):
    data = load_data()
    habits = data["habits"]
    habits.append(name.lower().strip())


def remove_habit(idx_habit):
    data = load_data()
    habits = data["habits"]
    del habits[idx_habit]


def edit_habit(idx_habit, name):
    data = load_data()
    habits = data["habits"]
    habits[idx_habit] = name


def habits():
    data = load_data()
    habits = data["habits"]
    habits_functions = data["habits_functions"]
    idx_option = get_user_input(habits_functions, msg="Select an option: ")

    if idx_option == 0:
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
        show_options(habits)
