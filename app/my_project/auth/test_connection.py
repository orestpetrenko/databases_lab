import pymysql

class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'orestiphone1234'
    MYSQL_DB = 'event_tickets'

# Тестове з'єднання
try:
    connection = pymysql.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB
    )
    print("✅ Connection to the database was successful!")
except Exception as e:
    print(f"❌ Error connecting to the database: {e}")
finally:
    if 'connection' in locals() and connection.open:
        connection.close()
        print("🔗 Connection closed.")
