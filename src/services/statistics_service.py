import pandas as pd

from src.database import load_data, save_data
from src.utils.clear_terminal import clear_terminal


def calculate_streaks():
    clear_terminal()
    data = load_data()
    records = data["records"]
    stats = data["habits_stats"]

    if not records:
        print("No records to calculate streaks.")
        _ = input("Press enter to continue...")
        return

    df_records = pd.DataFrame(records)
    df_records["date"] = pd.to_datetime(df_records["date"], format="%d-%m-%Y")
    df_records.sort_values(by="date", inplace=True)

    for habit in df_records["name"].unique():
        max_streak = stats[habit]["longest_streak"]
        current_streak = 1

        df_filtered = df_records[df_records["name"] == habit]

        for j in range(len(df_filtered) - 1):
            current_row = df_filtered.iloc[j]
            next_row = df_filtered.iloc[j + 1]

            diff = (next_row["date"] - current_row["date"]).days

            if (
                diff == 1
                and current_row["status"] == "completed"
                and next_row["status"] == "completed"
            ):
                current_streak += 1
            else:
                max_streak = max(max_streak, current_streak)
                current_streak = 1

        if max_streak > current_streak:
            stats[habit]["current_streak"] = current_streak
            stats[habit]["longest_streak"] = max_streak
        else:
            stats[habit]["current_streak"] = current_streak
            stats[habit]["longest_streak"] = current_streak

    save_data()
