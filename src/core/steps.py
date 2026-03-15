from src.services.steps_service import (
    create_step,
    edit_step,
    remove_step,
    show_steps,
)
from src.utils.clear_terminal import clear_terminal
from src.utils.options import steps_menu

ACTIONS = {
    "1": create_step,
    "2": edit_step,
    "3": remove_step,
    "4": show_steps,
}


def steps() -> None:
    clear_terminal()

    idx_menu = steps_menu()
    if idx_menu < 0 or idx_menu > len(ACTIONS):
        print("Invalid option. Please try again.")
        _ = input("Press enter to continue...")
        return

    action = ACTIONS.get(str(idx_menu))
    if action:
        action()
