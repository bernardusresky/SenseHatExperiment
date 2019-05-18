import sqlite3 as sqlite
from sqlite3 import Error

class Database:

    def __init__(self):
        self.db = "weather.db"

    def make_weather_table(self):
        weather_table = "CREATE TABLE IF NOT EXISTS weatherData (timestamp datetime, temperature integer, humidity integer, pressure integer, season string)"

        return weather_table

    def make_joystick_table(self):
        joystick_table = "CREATE TABLE IF NOT EXISTS joystickData (timestamp DATETIME, direction string, action string)"
        return joystick_table

    def open_connection(self):
        db = self.db
        try:
            conn = sqlite.connect(db)
            return conn
        except Error as e:
            print("Failt to connect to db")
            print(e)
        return None
    
    def close_connection(self, conn):
        conn.close()

    def table_create(self, conn, table):
        if conn is not None:
            try:
                c = conn.cursor()
                c.execute(table)
            except Error as e:
                print("Fail to create table")
                print(e)

    def commit_db(self, query, value):
        conn = self.open_connection()
        if conn is not None:
            c = conn.cursor()
            c.execute(query, value)
            c.commit()
            c.close()
            self.close_connection(conn)
    
    def get_db(self, query):
        conn = self.open_connection()
        if conn is not None:
            c = conn.cursor()
            c.execute(query)
            c.fetchall()
    
    def insert_into_weather(self, timestamp, temperature, humidity, pressure, season):
        query = """INSERT INTO TABLE weatherData (timestamp, temperature, humidity, pressure, season) 
                            VALUES (?, ?, ?, ?, ?))"""
        value = (timestamp, temperature, humidity, pressure, season)
        self.commit_db(query, value)
  
    def insert_into_joystick(self, timestamp, direction, action):
        query = """INSERT INTO TABLE joystickData (timestamp, direction, action) 
                        VALUES (?, ?, ?, ?))"""
        value = (timestamp, direction, action)
        self.commit_db(query, value)

def main():
    db = Database()
    j_table = db.make_joystick_table()
    w_table = db.make_weather_table()
    conn = db.open_connection()
    if conn is not None:
        db.table_create(conn, j_table)
        db.table_create(conn, w_table)
    else:
        print("fail!")

if __name__ == '__main__':
    main()