import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Goodnews2006",
  database="inventorycap_db"
)

cursor = db.cursor()
cursor.execute("SELECT * FROM low_stock_alerts")

for item in cursor.fetchall():
    print(f"ALERT: {item[1]} is low! Current stock: {item[2]}")