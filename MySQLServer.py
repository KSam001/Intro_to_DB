import mysql.connector
from mysql.connector import errorcode

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'your_new_password'

DB_NAME = 'alx_book_store'

def create_database():
    """Connects to MySQL server and creates a database."""
    try:
        cn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = cn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(DB_NAME))
        print(f"Database '{DB_NAME}' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        if 'cn' in locals() and cn.is_connected():
            cursor.close()
            cn.close()

if __name__ == "__main__":
    create_database()
