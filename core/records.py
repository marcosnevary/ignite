from datetime import datetime

from core.repository import load_data
from core.utils import get_user_input, show_options


def create_record(idx_habit, idx_status):
    data = load_data()
    habits = data["habits"]
    records = data["records"]
    status = data["status"]
    records.append(
        {
            "date": datetime.now().strftime("%d-%m-%Y"),
            "name": habits[idx_habit].lower().strip(),
            "status": status[idx_status],
        }
    )


def remove_record(idx_record):
    data = load_data()
    records = data["records"]
    del records[idx_record]


def edit_record(idx_record, idx_habit, idx_status):
    data = load_data()
    habits = data["habits"]
    records = data["records"]
    status = data["status"]
    records[idx_record] = {
        "date": datetime.now().strftime("%d-%m-%Y"),
        "name": habits[idx_habit].lower().strip(),
        "status": status[idx_status],
    }


def records():
    data = load_data()
    records_actions = data["records_functions"]
    habits = data["habits"]
    status = data["status"]
    records = data["records"]

    idx_option = get_user_input(records_actions, msg="Select an option: ")
    if idx_option == 0:
        idx_habit = get_user_input(habits, msg="Select the habit to record: ")
        idx_status = get_user_input(status, msg="Select the status of the record: ")
        create_record(idx_habit, idx_status)
    if idx_option == 1:
        idx_record = get_user_input(records, msg="Select the record to edit: ")
        idx_new_habit_name = get_user_input(
            habits, msg="Select the new habit for the record: "
        )
        idx_new_status = get_user_input(
            status, msg="Select the new status for the record: "
        )
        edit_record(idx_record, idx_new_habit_name, idx_new_status)
    if idx_option == 2:
        idx_record = get_user_input(records, msg="Select the record to remove: ")
        remove_record(idx_record)
    if idx_option == 3:
        show_options(records)
