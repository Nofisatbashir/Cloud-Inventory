import mysql.connector
import yfinance as yf
#1. Connect to your local MySQL server
db = mysql.connector.connect(host="localhost", user="root", password="Goodnews2006", database="inventory_db")
def log_stock_price(ticker)
    #2. Get live data
cursor = db.cursor()
    stock = yf.Ticker(ticker)
    price =stock.fast_info['last_price'] 
        #3. Prepare the SQl command
        sql = "INSERT INTO stock_tracking(ticker, price) VALUES (%s, %s)"
        val = (ticker, price)
        #4. Execute and save
        cursor.execute(sql, val)
        db.commit()
        print(f"Successfully saved {ticker}at $ price to the database!")
        # Test it
        log_stock_price("AAPL")