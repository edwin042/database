import mysql.connector
from mysql.connector import errorcode

config = {'user': 'root', 'password': 'root', 'host': 'localhost', 'port': '8889'}
mysql_conn = mysql.connector.connect(**config)
cursor = mysql_conn.cursor()
DB_NAME = 'owmdata'


def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        mysql_conn.database = DB_NAME
    else:
        print(err)
        exit(1)

cursor.close()
mysql_conn.close()
