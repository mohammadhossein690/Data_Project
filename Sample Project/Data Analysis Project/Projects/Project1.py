# Choropleth maps
# first we do import our needed modules
import  chart_studio.plotly as py
import pandas as pd
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
import plotly.graph_objects as go

# Then we go to setup
# init_notebook_mode(connected=True)
df = pd.read_csv(r'C:\Users\NoteBook\Desktop\Sample Project\Data Analysis Project\Projects\csv files\2014_World_Power_Consumption')
print(df.head())

# We create our choropleth maps
data = dict(type = 'choropleth',colorscale = 'Viridis',reversescale = True,locations = df['Country'],
        locationmode = "country names",z = df['Power Consumption KWH'],text = df['Country'],
        colorbar = {'title' : 'Power Consumption KWH'})

layout = dict(title = '2014 Power Consumption KWH',
                geo = dict(showframe = False,projection = {'type':'equirectangular'})
             )



layout = dict(title='2014 World Power Consumption',geo=dict(showframe=False,projection={'type':'natural earth'}))

choro_map = go.Figure(data=[data],layout=layout)
iplot(choro_map)

