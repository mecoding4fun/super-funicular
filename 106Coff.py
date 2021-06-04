import pandas as pd
import plotly.express as px
import csv
import numpy as np

def getDataSource():
    sleepInHours=[]
    coffee=[]
    with open('Coffee.csv') as f:
        data= csv.DictReader(f)
        for a in data:
            sleepInHours.append(float(a['sleep in hours']))
            coffee.append(float(a['Coffee in ml']))
        return {'x': coffee,'y': sleepInHours}

def FindCorelation(DataSource):
    corelation = np.corrcoef(DataSource['x'],DataSource['y'])
    print(corelation[0,1])

def setup():
    DataSource = getDataSource()
    FindCorelation(DataSource)

setup()
