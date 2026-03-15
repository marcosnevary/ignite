from src.core.goals import goals
from src.core.steps import steps
from src.core.timer import timer
from src.database import save_data
from src.utils.clear_terminal import clear_terminal
from src.utils.options import main_menu

ACTIONS = {
    "1": goals,
    "2": steps,
    "3": timer,
}


def main() -> None:
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
