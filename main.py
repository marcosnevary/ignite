from src.core.habits import habits
from src.core.records import records
from src.core.statistics import statistics
from src.database import save_data
from src.utils.clear_terminal import clear_terminal
from src.utils.options import main_menu

ACTIONS = {
    "1": habits,
    "2": records,
    "3": statistics,
}


def main():
    while True:
        clear_terminal()
        idx_menu = main_menu()

        if idx_menu < 1 or idx_menu > len(ACTIONS):
            break

        action = ACTIONS.get(str(idx_menu))
        if action:
            action()
    save_data()


if __name__ == "__main__":
    main()
