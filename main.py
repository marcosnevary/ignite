from core.habits import habits
from core.records import records
from core.repository import load_data, save_data
from core.utils import get_user_input


def main():
    data = load_data()
    menus = data["menus"]
    while True:
        user_input = get_user_input(menus)
        if user_input == -1:
            break
        if user_input == 0:
            habits()
        if user_input == 1:
            records()
    save_data()


if __name__ == "__main__":
    main()
