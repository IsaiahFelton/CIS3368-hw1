from ContactData import contactData
import datetime
from datetime import date
import mysql.connector
from mysql.connector import Error

# Creating connection to with AWS(code was referenced from Professor Otto in his in class example)
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )  
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# Executing the info from the query as a string once the connection is established with AWS(code was referenced from Professor Otto in his in class example)
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
# Executing query to fetch all the info from the called table once the connection is established with AWS(code was referenced from Professor Otto in his in class example)
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


# Personal connection
connection = create_connection("cis3368v5.cwb2r4cwyvi9.us-east-2.rds.amazonaws.com", "admin", "Wolfpack69!", "cis3368db")


# Selecting all the info from my contacts table in MySql
select_contacts = "SELECT * FROM contacts"
contacts = execute_read_query(connection, select_contacts)

