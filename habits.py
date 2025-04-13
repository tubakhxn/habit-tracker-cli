### File: habits.py
from db import get_connection
from datetime import datetime


def add_habit(name):
    with get_connection() as conn:
        conn.execute("INSERT OR IGNORE INTO habits (name, last_done) VALUES (?, ?)", (name, None))


def complete_habit(name):
    today = datetime.today().strftime('%Y-%m-%d')
    with get_connection() as conn:
        habit = conn.execute("SELECT id FROM habits WHERE name = ?", (name,)).fetchone()
        if habit:
            conn.execute("INSERT INTO completions (habit_id, date) VALUES (?, ?)", (habit['id'], today))
            conn.execute("UPDATE habits SET last_done = ? WHERE id = ?", (today, habit['id']))


def list_habits():
    with get_connection() as conn:
        habits = conn.execute("SELECT name, last_done FROM habits").fetchall()
        return [dict(row) for row in habits]