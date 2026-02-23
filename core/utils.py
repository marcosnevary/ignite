import os


def show_options(options, title="", format="enumerate"):
    print("=" * 64)
    if title:
        print(title)
    for i, option in enumerate(options, start=1):
        print(
            f"{str(i) + '.' if format == 'enumerate' else '-'} {option.replace('_', ' ').title() if isinstance(option, str) else option}"
        )


def get_user_input(options, msg=""):
    show_options(options)
    print("=" * 64)
    user_input = int(input(msg))

    return user_input - 1


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
