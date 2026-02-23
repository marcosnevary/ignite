from src.services.records_service import (
    create_record,
    edit_record,
    remove_record,
    show_records,
)
from src.utils.clear_terminal import clear_terminal
from src.utils.options import records_menu

ACTIONS = {
    "1": create_record,
    "2": edit_record,
    "3": remove_record,
    "4": show_records,
}


def records():
    clear_terminal()

    idx_menu = records_menu()
    if idx_menu < 1 or idx_menu > len(ACTIONS):
        print("Invalid option. Please try again.")
        _ = input("Press enter to continue...")
        return

    action = ACTIONS.get(str(idx_menu))
    if action:
        action()
