from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="oyeendamola2",  
    database="inventory_db"     
)

cursor = db.cursor()

@app.route('/')
def index():
    return "Flask is connected to MySQL!"

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    val = (name, email)
    cursor.execute(sql, val)
    db.commit()
    return "User added successfully!"

if __name__ == "__main__":
    app.run(debug=True)