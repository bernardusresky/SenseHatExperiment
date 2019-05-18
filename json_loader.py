import json

class ReadJson():

    def open(self):
        with open('weather_config.json', 'r') as weather_file:
            weather_config = json.loads(weather_file)
            winterMtemperature = weather_config["winter_min_temperature"]
            winterPtemperature = weather_config["winter_max_temperature"]
            summerMtemperature = weather_config["summer_min_temperature"]
            summerPtemperature = weather_config["summer_max_temperature"]
            autumnMtemperature = weather_config["autumn_min_temperature"]
            autumnPtemperature = weather_config["autumn_max_temperature"]
            springMtemperature = weather_config["springPtemperature"]
            springPtemperature = weather_config["springPtemperature"]
            min_humidity = weather_config["min_humidity"]
            max_humidity = weather_config["max_humidity"]
        weather_file.close()
        return winterMtemperature, winterPtemperature, summerMtemperature, summerPtemperature, autumnMtemperature, autumnPtemperature, springMtemperature, springPtemperature, min_humidity, max_humidity