from src.services.goals_service import (
    create_goal,
    edit_goal,
    remove_goal,
    show_goals,
)
from src.utils.clear_terminal import clear_terminal
from src.utils.options import goals_menu

ACTIONS = {
    "1": create_goal,
    "2": edit_goal,
    "3": remove_goal,
    "4": show_goals,
}


def goals() -> None:
    clear_terminal()

    idx_menu = goals_menu()
    if idx_menu < 0 or idx_menu > len(ACTIONS):
        print("Invalid option. Please try again.")
        _ = input("Press enter to continue...")
        return

    action = ACTIONS.get(str(idx_menu))
    if action:
        action()
