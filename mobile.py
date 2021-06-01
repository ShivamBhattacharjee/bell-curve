import plotly.express as px 
import plotly.figure_factory as ff 
import pandas as pd
import csv

df1=pd.read_csv("mobile.csv")
fig1=ff.create_distplot([df1["Avg Rating"].tolist()],["avg rating"],show_hist=False)
fig1.show()