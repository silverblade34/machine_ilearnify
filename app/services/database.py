import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'mysql+mysqlconnector://sysnet:Sys4Log$$sa@67.207.87.64/udemy'

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="67.207.87.64",
            user="sysnet",
            password="Sys4Log$$sa",
            database="udemy"
        )
        if connection.is_connected():
            print("Connected to the database")
        return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def get_sqlalchemy_session():
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session, engine
