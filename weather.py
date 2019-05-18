from sense_hat import SenseHat
from db import Database
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
            timestamp = time.strftime('%m-%d-%Y %H-%M-%S')
            date = time.strftime('%m-%d')
            season = self.season_checker(date)
            db.insert_into_weather(timestamp, temperature, humidity, pressure, season)

    def season_checker(self, date):
        if (date >= 12-1 and date <= 2-28):
            season = "summer"
            return season
        elif (date >= 3/1 and date <= 5/31):
            season = "autumn"
            return season
        elif (date >= 6/1 and date <= 8/31):
            season = "winter"
            return season
        elif (date >= 9/1 and date <= 11/30):
            season = "spring"
            return season

    def temp_hum_checker(self, season, temp, hum):
        json = self.rjson

        (wMinTemperature, wMaxTemperature, suMinTemperature, suMaxTemperature, auMinTemperature, auMaxTemperature, spMinTemperature, spMaxTemperature, minHumidity, maxHumidity) = json.open()
        if season == "summer":
            if (temp < suMinTemperature or temp > suMaxTemperature):
                status = "Not Okay"
                return status
            else:
                status = "Okay"
                return status
        if season == "autumn":
            if (temp < auMinTemperature or temp > auMaxTemperature):
                status = "Not Okay"
                return status
            else:
                status = "Okay"
                return status
        if season == "spring":
            if (temp < spMinTemperature or temp > spMaxTemperature):
                status = "Not Okay"
                return status
            else:
                status = "Okay"
                return status
        if season == "winter":
            if (temp < wMinTemperature or temp > wMaxTemperature):
                status = "Not Okay"
                return status
            else:
                status = "Okay"
                return status
        if (hum < minHumidity or hum > maxHumidity):
            humStatus = "Not Okay"
            return humStatus
        else:
            humStatus = "Okay"
            return humStatus

def main():

    sensenv = SenseEnv()
    sensenv.insert_env_data()
    print("Script successfully runned")


if __name__ == '__main__':
    main()
        
