from db import get_connection
from datetime import datetime, timedelta

def get_all_stats():
    with get_connection() as conn:
        habits = conn.execute("SELECT id, name FROM habits").fetchall()
        stats = {}
        for habit in habits:
            completions = conn.execute(
                "SELECT date FROM completions WHERE habit_id = ? ORDER BY date DESC",
                (habit['id'],)
            ).fetchall()
            dates = [datetime.strptime(row['date'], '%Y-%m-%d') for row in completions]
            streak = calculate_streak(dates)
            stats[habit['name']] = streak
        return stats

def calculate_streak(dates):
    if not dates:
        return 0

    streak = 1
    for i in range(1, len(dates)):
        delta = (dates[i-1] - dates[i]).days
        if delta == 1:
            streak += 1
        else:
            break
    return streak
