from flask import Flask, render_template, request, redirect, url_for
from habits import add_habit, complete_habit, list_habits
from stats import get_all_stats
from db import init_db

app = Flask(__name__)

@app.route('/')
def index():
    habits = list_habits()
    stats = get_all_stats()
    return render_template('index.html', habits=habits, stats=stats)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('habit')
    if name:
        add_habit(name)
    return redirect(url_for('index'))

@app.route('/done/<habit_name>')
def done(habit_name):
    complete_habit(habit_name)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
