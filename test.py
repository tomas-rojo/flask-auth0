
import psycopg2
from psycopg2 import Error
import os
from dotenv import load_dotenv

load_dotenv()

def create_connection():
    connection = psycopg2.connect(
        dbname=os.getenv('PG_DBNAME'),
        user=os.getenv('PG_USER'),
        password=os.getenv('PG_PASS'),
        host=os.getenv('PG_HOST'),
        port=os.getenv('PG_PORT'))
    return connection

# Connection to DDBB to insert data

# def insert_data(name, value):
#     try:
#         # Connect to Database
#         conn = create_connection()
#         cursor = conn.cursor()

#         # Inserting and Executing Query
#         db_name = os.getenv('PG_DBNAME')
#         cursor.execute("INSERT INTO {} VALUES (%s, %s)".format(db_name), (name, value,))
#         conn.commit()

#         conn.close()

#     except:
#         print("Couldn't insert values to Database")


def get_user(user_id):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users where id_ = '{user_id}'")
        res = cursor.fetchone()
        return res
        
    except Error as e:
        print(e)

    
def add_new_user(id_, name, email, profile_pic):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        query = f""" INSERT INTO users VALUES(
                    '{id_}', 
                    '{name}', 
                    '{email}', 
                    '{profile_pic}')
                """
        cursor.execute(query)
        print
        conn.commit()
        
    except Error as e:
        print(e)