import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    operators = conn.execute('SELECT * FROM operators').fetchall()
    conn.close()
    return render_template('index.html', operators=operators)


@app.route('/listPlans', methods=('GET', 'POST'))
def list_plans():
    if request.method == 'POST':
        operator = request.form['operator']
        circle = request.form['circle']
        conn = get_db_connection()
        plans = conn.execute("SELECT * FROM plans WHERE operator=? AND circle_name=?", (operator, circle)).fetchall()
        operators = conn.execute('SELECT * FROM operators').fetchall()
        circles = conn.execute('SELECT distinct circle_name FROM plans WHERE operator=?', (operator, )).fetchall()
        return render_template('list-plans.html', selected_operator=operator, selected_circle=circle, plans=plans, operators=operators, circles=circles)

@app.route('/circles')
def list_circles():
    conn = get_db_connection()
    operator = request.args.get('operator')
    operators = conn.execute('SELECT * FROM operators').fetchall()
    circles = conn.execute('SELECT distinct circle_name FROM plans WHERE operator=?', (operator, )).fetchall()
    conn.close()
    return render_template('select-circle.html', operators=operators, circles=circles, selected_operator=operator)