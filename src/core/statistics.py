from src.services.statistics_service import calculate_streaks
from src.utils.clear_terminal import clear_terminal
from src.utils.options import statistics_menu

ACTIONS = {
    "1": calculate_streaks,
}


def statistics():
    clear_terminal()

    idx_menu = statistics_menu()
    if idx_menu < 1 or idx_menu > len(ACTIONS):
        print("Invalid option. Please try again.")
        _ = input("Press enter to continue...")
        return

    action = ACTIONS.get(str(idx_menu))
    if action:
        action()
