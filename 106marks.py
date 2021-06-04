import pandas as pd
import plotly.express as px
import csv
import numpy as np

def getDataSource():
    Marks=[]
    DaysPresent=[]
    with open('Marks.csv') as f:
        data= csv.DictReader(f)
        for a in data:
            Marks.append(float(a['Marks In Percentage']))
            DaysPresent.append(float(a['Days Present']))
        return {'x': DaysPresent,'y': Marks}

def FindCorelation(DataSource):
    corelation = np.corrcoef(DataSource['x'],DataSource['y'])
    print(corelation[0,1])

def setup():
    DataSource = getDataSource()
    FindCorelation(DataSource)

setup()
