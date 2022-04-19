


from asyncio.windows_events import NULL
import mysql.connector
from mysql.connector import Error
import json



def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection



def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection



def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def execute_valued_query( query, val):
    cursor = connection.cursor()
    try:
        cursor.execute(query, val)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


connection = create_server_connection("localhost", "root", 'burak')

create_database(connection, "CREATE DATABASE json2sql")



create_table = """
CREATE TABLE names (
  id INT ,
  id2 INT ,
  name VARCHAR(20)
  );
 """


connection = create_db_connection("localhost", "root", 'burak', 'json2sql') # Connect to the Database
execute_query(connection, create_table) # Execute our defined query

isim = "burak"

# sql = 'INSERT INTO names(id, id2, name) VALUES({}, {}, {})'.format(126,3, "haci") 
# sql = """INSERT INTO names VALUES(1,  2 , {isim});""".format("ahmet")
# print(sql)


sql = "INSERT INTO names(id, id2, name) VALUES(%d, %d, %s)"
val = (45, 999, "burakgun")

connection = create_db_connection("localhost", "root", 'burak', 'json2sql') # Connect to the Database
execute_valued_query(sql, val)