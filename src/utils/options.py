from src.database import load_data


def list_habits():
    data = load_data()
    habits = data["habits"]

    print("=" * 64)
    for idx, habit in enumerate(habits):
        print(f"{idx + 1}. {habit.replace('_', ' ').title()}")
    print("=" * 64)


def list_records():
    data = load_data()
    records = data["records"]

    print("=" * 64)
    for record in records:
        print(
            f"- {record['date']} - {record['name'].replace('_', ' ').title()} - {record['status'].replace('_', ' ').title()}"
        )
    print("=" * 64)


def list_status():
    data = load_data()
    status = data["status"]

    print("=" * 64)
    for idx, stat in enumerate(status):
        print(f"{idx + 1}. {stat.replace('_', ' ').title()}")
    print("=" * 64)


def main_menu():
    print("=" * 64)
    print("1. Habits")
    print("2. Records")
    print("=" * 64)
    return int(input("Enter the number of the option you want to select: "))


def habits_menu():
    print("=" * 64)
    print("1. Create a new habit")
    print("2. Edit an existing habit")
    print("3. Remove an existing habit")
    print("4. Show all habits")
    print("=" * 64)
    return int(input("Enter the number of the option you want to select: "))


def records_menu():
    print("=" * 64)
    print("1. Create a new record")
    print("2. Edit an existing record")
    print("3. Remove an existing record")
    print("4. Show all records")
    print("=" * 64)
    return int(input("Enter the number of the option you want to select: "))
