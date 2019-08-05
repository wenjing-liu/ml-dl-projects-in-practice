#%%
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot, plot
init_notebook_mode(connected=True)

#%%
df = pd.read_csv('2014_World_Power_Consumption')

#%%
df.head()

#%%
data = dict(type='choropleth',
  locations=df['Country'],
  z=df['Power Consumption KWH'],
  locationmode = "country names",
  text=df['Country'],
  colorbar={'title': '2014 World Power Consumption'}
  )
layout = dict(title='2014 World Power Consumption',
  geo = dict(showframe=False, projection={'type': 'kavrayskiy7'})
  )
choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)

#%%
choromap = go.Figure(data = [data],layout = layout)
plot(choromap,validate=False)

#%%
usdf = pd.read_csv('2012_Election_Data')
usdf.head()

#%%
data = dict(type='choropleth',
            colorscale = 'Viridis',
            reversescale = True,
            locations = usdf['State Abv'],
            z = usdf['Voting-Age Population (VAP)'],
            locationmode = 'USA-states',
            text = usdf['State'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 1)),
            colorbar = {'title':"Voting-Age Population (VAP)"}
            )
layout = dict(title = '2012 General Election Voting Data',
              geo = dict(scope='usa',
                         showlakes = True,
                         lakecolor = 'rgb(85,173,240)')
             )
choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)

#%%
