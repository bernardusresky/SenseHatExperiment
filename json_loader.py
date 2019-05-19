import json

class ReadJson():

    def open(self):
        with open('weather_config.json', 'r') as weather_file:
            weather_config = json.load(weather_file)
            min_temperature = weather_config["min_temperature"]
            max_temperature = weather_config["max_temperature"]
            min_humidity = weather_config["min_humidity"]
            max_humidity = weather_config["max_humidity"]
        weather_file.close()
        return min_temperature, max_temperature, min_humidity, max_humidity