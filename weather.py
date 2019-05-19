from sense_hat import SenseHat
from db import Database
from datetime import datetime
import time
from json_loader import ReadJson

class SenseEnv:
    
    def __init__(self):
        self.sense = SenseHat()
        self.db = Database()
        self.rjson = ReadJson()

    def get_env_data(self):
        sense = self.sense
        temperature = int(sense.get_temperature())
        humidity = int(sense.get_humidity())
        pressure = int(sense.get_pressure())

        return temperature, humidity, pressure

    def insert_env_data(self):
        db = self.db

        (temperature, humidity, pressure) = self.get_env_data()
        
        while (temperature is not 0 and humidity is not 0 and pressure is not 0):
            time.sleep(10)
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            status = self.temp_hum_checker(temperature, humidity)
            db.insert_into_weather(timestamp, temperature, humidity, pressure, status)
            #remember to delete this print(just for test)
            print("successfully insert data")

    def temp_hum_checker(self, temp, hum):
        json = self.rjson

        (min_temperature, max_temperature, minHumidity, maxHumidity) = json.open()
        
        if (temp < min_temperature or temp > max_temperature):
            status = "Not Okay"
        else:
            status = "Okay"

        if (hum < minHumidity or hum > maxHumidity):
            humStatus = "Not Okay"
        else:
            humStatus = "Okay"
        
        combinestatus = status + humStatus
        return combinestatus

def main():

    sensenv = SenseEnv()
    sensenv.insert_env_data()
    print("Script successfully runned")


if __name__ == '__main__':
    main()
        
