from db import Database
import pandas as pd
import seaborn
import bokeh
import plotly

class GraphVirtualization():

    def __init__(self):
        self.db = Database()
    
    def get_data(self, time):
        db = self.db
        datas = db.get_weather(time)
        labels = ['Timestamp', 'Temperature(C)', 'Humidity(%)', 'Pressure', 'Status']
        df = pd.DataFrame(datas, columns=labels)
        print(df) 
        return df
              

    def seaborn_graph(self, data):
        pass

    def bokeh_graph(self, data):
        pass

    def plotly_graph(self, data):
        pass
