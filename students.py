import pandas as py
import plotly.express as px
import csv

df = py.read_csv('/Users/prathamarora/Downloads/Python_Projects/data_analization_and_visualization/data.csv')

mean = df.groupby('level')['attempt'].mean()

figure = px.scatter(df , x = 'student_id', y = 'level', color = 'attempt', size = 'attempt')

figure.show()