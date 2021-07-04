import pandas as pd,plotly_express as px
Data = pd.read_csv("Copyofdata.csv")
graph = px.scatter(Data,x = "date" , y = "cases", color="country", size = "cases")
graph.show()