import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        dbname='Davron',
        user='your_user',
        password='your_password',
        host='localhost'
    )


@app.route('/')
def index():
    level = request.args.get('level', 'Undergraduate')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM courses WHERE level = %s;", (level,))
    courses = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', courses=courses, level=level)
