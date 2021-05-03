import numpy as np
import csv
import plotly.express as px
import pandas as pd

def getDataSource(path):
    cups_of_coffee = []
    hours_of_sleep = []

    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            cups_of_coffee.append(float(row["Coffee (in ml)"]))
            hours_of_sleep.append(float(row["Sleep (in hours)"]))
    
    return {"x" : cups_of_coffee, "y" : hours_of_sleep}

def findCorrelation(source_of_data):
    correlation = np.corrcoef(source_of_data["x"], source_of_data["y"])
    print("The correlation between cups of coffee (ml) and hours of sleep is:\n", correlation[0, 1])

def plotFigure(path, x_co, y_co):
    data_frame = pd.read_csv(path)
    #plotting correlation as a trendline
    plot = px.scatter(data_frame, x = x_co, y = y_co, trendline = 'ols')
    plot.show()

def setup():
    path = "C:/Users/sravy/White Hat Jr/Project 106- Correlation/cups of coffee vs hours of sleep.csv"
    source = getDataSource(path)
    findCorrelation(source)
    plotFigure("C:/Users/sravy/White Hat Jr/Project 106- Correlation/cups of coffee vs hours of sleep.csv", "Coffee (in ml)", "Sleep (in hours)")

setup()