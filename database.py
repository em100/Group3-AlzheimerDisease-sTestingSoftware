import mysql.connector
from mysql.connector import Error

class Database:
    """Handles database connections and operations."""

    @staticmethod
    def connect_db():
        """
        Establishes a connection to the MySQL database.
        Returns:
            connection: A MySQL connection object or None if connection fails.
        """

        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='alzheimer_testing',
                user='root',
                password='emus100M!'
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print("Error while connecting to MySQL", e)
        return None