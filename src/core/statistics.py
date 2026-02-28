from src.database import load_data
from src.services.statistics_service import calculate_streaks
from src.utils.clear_terminal import clear_terminal
from src.utils.options import list_habits, list_stats


def statistics():
    clear_terminal()
    data = load_data()
    habits = data["habits"]

    calculate_streaks()

    list_habits()
    idx_habit = int(input("Select the habit to view stats (number): ")) - 1

    if idx_habit < 0 or idx_habit >= len(habits):
        print("Invalid habit number.")
        _ = input("Press enter to continue...")
        return

    list_stats(habits[idx_habit])
    _ = input("Press enter to continue...")
