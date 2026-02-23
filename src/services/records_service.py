from datetime import datetime

from src.database import load_data, save_data
from src.utils.clear_terminal import clear_terminal
from src.utils.options import list_habits, list_records, list_status


def create_record():
    clear_terminal()
    data = load_data()
    habits = data["habits"]
    records = data["records"]
    status = data["status"]

    if not habits:
        print("No habits to record.")
        _ = input("Press enter to continue...")
        return

    list_habits()

    idx_habit = int(input("Select the habit to record (number): ")) - 1
    if not (0 <= idx_habit < len(habits)):
        print("Invalid habit number.")
        _ = input("Press enter to continue...")
        return

    list_status()

    idx_status = int(input("Select the status of the habit (number): ")) - 1
    if not (0 <= idx_status < len(status)):
        print("Invalid status number.")
        _ = input("Press enter to continue...")
        return

    records.append(
        {
            "date": datetime.now().strftime("%d-%m-%Y"),
            "name": habits[idx_habit].lower().strip(),
            "status": status[idx_status],
        }
    )
    save_data()


def remove_record():
    clear_terminal()
    data = load_data()
    records = data["records"]

    if not records:
        print("No records to remove.")
        _ = input("Press enter to continue...")
        return

    list_records()
    idx_record = int(input("Select the record to remove (number): ")) - 1
    if not (0 <= idx_record < len(records)):
        print("Invalid record number.")
        _ = input("Press enter to continue...")
        return

    del records[idx_record]
    save_data()


def edit_record():
    clear_terminal()
    data = load_data()
    habits = data["habits"]
    records = data["records"]
    status = data["status"]

    if not records:
        print("No records to edit.")
        _ = input("Press enter to continue...")
        return

    list_records()
    idx_record = int(input("Select the record to edit (number): ")) - 1
    if not (0 <= idx_record < len(records)):
        print("Invalid record number.")
        _ = input("Press enter to continue...")
        return

    list_habits()
    idx_habit = int(input("Select the new habit for the record (number): "))
    if not (0 <= idx_habit < len(habits)):
        print("Invalid habit number.")
        _ = input("Press enter to continue...")
        return

    list_status()
    idx_status = int(input("Select the new status for the record (number): "))
    if not (0 <= idx_status < len(status)):
        print("Invalid status number.")
        _ = input("Press enter to continue...")
        return

    records[idx_record] = {
        "date": records[idx_record]["date"],
        "name": habits[idx_habit].lower().strip(),
        "status": status[idx_status],
    }
    save_data()


def show_records():
    clear_terminal()
    data = load_data()
    records = data["records"]

    if not records:
        print("No records found.")
        _ = input("Press enter to continue...")
        return

    list_records()
    _ = input("Press enter to continue...")
