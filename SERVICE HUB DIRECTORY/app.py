import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ---------------- DATABASE CONNECTION ----------------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="service_hub"
    )

# ---------------- LOGIN PAGE ----------------
@app.route('/')
def login_page():
    return render_template('login.html')

# ---------------- LOGIN PROCESS ----------------
@app.route('/login', methods=['POST'])
def login():
    return redirect(url_for('register'))

# ---------------- REGISTER PAGE ----------------
@app.route('/register')
def register():
    return render_template('register.html')

# ---------------- SAVE USER TO DATABASE ----------------
@app.route('/register', methods=['POST'])
def register_post():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (name, email, phone, password)
        VALUES (%s, %s, %s, %s)
    """, (name, email, phone, password))

    conn.commit()
    conn.close()

    return redirect(url_for('home'))

# ---------------- HOME PAGE ----------------
@app.route('/home')
def home():
    return render_template('home.html')

# ---------------- RUN APP ----------------
if __name__ == '__main__':
    app.run(debug=True)