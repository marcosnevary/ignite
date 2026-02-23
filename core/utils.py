def show_options(options):
    print("===============================")
    for i, option in enumerate(options, start=1):
        print(
            f"{i}. {option.replace('_', ' ').title() if isinstance(option, str) else option}"
        )
    print("===============================")


def get_user_input(options, msg=""):
    show_options(options)
    user_input = int(input(msg))
    return user_input - 1 if user_input > 0 else -1
