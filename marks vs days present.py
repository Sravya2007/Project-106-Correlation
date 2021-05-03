import numpy as np
import csv
import plotly.express as px
import pandas as pd

def getDataSource(path):
    student_marks = []
    days_present = []

    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            student_marks.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    
    return {"x" : student_marks, "y" : days_present}

def findCorrelation(source_of_data):
    correlation = np.corrcoef(source_of_data["x"], source_of_data["y"])
    print("The correlation between student marks and days present is:\n", correlation[0, 1])

def plotFigure(path, x_co, y_co):
    data_frame = pd.read_csv(path)
    #plotting correlation as a trendline
    plot = px.scatter(data_frame, x = x_co, y = y_co, trendline = 'ols')
    plot.show()

def setup():
    path = "C:/Users/sravy/White Hat Jr/Project 106- Correlation/student marks vs days present.csv"
    source = getDataSource(path)
    findCorrelation(source)
    plotFigure("C:/Users/sravy/White Hat Jr/Project 106- Correlation/student marks vs days present.csv", "Marks In Percentage", "Days Present")

setup()