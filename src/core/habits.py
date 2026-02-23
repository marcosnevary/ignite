from src.services.habits_service import (
    create_habit,
    edit_habit,
    remove_habit,
    show_habits,
)
from src.utils.clear_terminal import clear_terminal
from src.utils.options import habits_menu

ACTIONS = {
    "1": create_habit,
    "2": edit_habit,
    "3": remove_habit,
    "4": show_habits,
}


def habits():
    clear_terminal()

    idx_menu = habits_menu()
    if idx_menu < 1 or idx_menu > len(ACTIONS):
        print("Invalid option. Please try again.")
        _ = input("Press enter to continue...")
        return

    action = ACTIONS.get(str(idx_menu))
    if action:
        action()
