# Choropleth maps
# first we do import our needed modules
import  chart_studio.plotly as py
import pandas as pd
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
import plotly.graph_objects as go

# Then we go to setup
# init_notebook_mode(connected=True)
df = pd.read_csv(r'C:\Users\NoteBook\Desktop\Sample Project\Data Analysis Project\Projects\csv files\2012_Election_Data')
print(df.head())


# We create our choropleth maps
data = dict(type='choropleth',locations=df['State Abv'],locationmode='USA-states',
        colorscale='YlOrRd',z=df['Voting-Age Population (VAP)'] ,text = df['State'],
        colorbar={'title':'Numbers of people that vote'},marker=dict(line=dict(color='rgb(12,12,12)',width=2)))

layout = dict(title='2012 Election\'s Data',geo=dict(scope='usa',showlakes=True,lakecolor='rgb(85,173,240)'))

choro_map = go.Figure(data=[data],layout=layout)
iplot(choro_map)
