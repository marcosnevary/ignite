from src.services.timer_service import configure_timer, start_timer
from src.utils.clear_terminal import clear_terminal
from src.utils.options import timer_menu

ACTIONS = {
    "1": configure_timer,
    "2": start_timer,
}


def timer():
    clear_terminal()

    idx_menu = timer_menu()
    if idx_menu < 0 or idx_menu > len(ACTIONS):
        print("Invalid option. Please try again.")
        _ = input("Press enter to continue...")
        return

    action = ACTIONS.get(str(idx_menu))
    if action:
        action()
