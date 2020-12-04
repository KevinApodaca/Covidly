from apis import covid_daily_api
import plotly
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html


#   NOTES: 
#     - Used Sourcerree to merge 'Trelo-12-covidAPI' into 'Trello-24-mirrored_barchart' to get the updated covi_daily_api.py file 
#     - needs further testing

texas_counties = ['Harris', 'Dallas', 'Tarrant', 'Bexar', 'Travis', 'Collin', 'Denton', 'Hidalgo', 'El Paso', 'Fort Bend']


allCountiesCases = []
for county in texas_counties:
    county_cases = covid_daily_api.casesCounty(county, "Texas")
    allCountiesCases.append(county_cases)
print(allCountiesCases)

allCountiesDeaths = []
for county in texas_counties:
    county_death = covid_daily_api.deathsCounty(county, "Texas")
    allCountiesDeaths.append(county_death)
print(allCountiesDeaths)

citiesArr = ['Houston','San Antonio','Dallas', 'Austin', 'Fort Worth', 
    'El Paso', 'Arlington', 'Corpus Cristi', 'Plano', 'Laredo']

    # -- implement API calls to avoid hard code data
cases = [3270, 2400, 1200, 1400, 2420, 3000, 900, 700, 800, 1000] #can set cases=allCountiesCases rather than sample data or change in trace x axis
deaths = [320, 230,  455,  830, 350, 350, 300, 215, 610, 665]     #can set deaths=allCountiesDeaths rather than sample data or change in trace x axis and neg_deaths

    # -- loop ready for API call implemetation (assuming data returns a single number), just need to set: cases, deaths = []
#for city in citiesArr:
#    cases.append( getdata.usa_cityCases(city) )
#    deaths.append( getdata.usa_cityDeaths(city) )

neg_deaths = []

for i in range(len(deaths)):
    neg_deaths.append( deaths[i]*-1 )

fig = go.Figure()

fig.add_trace(go.Bar(x=cases[::-1], y=citiesArr[::-1], #replace cittiesArr with texas_counties
                base=0,
                marker_color='orange',
                name='Cases',
                orientation='h',
                text = cases[::-1],
                textposition = 'inside',
                insidetextanchor = 'start',
                hoverinfo = 'y',                #change to 'none' to disable bar hover text
                ) )
fig.add_trace(go.Bar(x=neg_deaths[::-1], y=citiesArr[::-1],  #replace cittiesArr with texas_counties
                base=0,
                marker_color='crimson',
                name='Deaths',
                orientation='h',
                text = deaths[::-1],
                textposition = 'inside',
                insidetextanchor = 'start',
                hoverinfo = 'y',                #change to 'none' to disable bar hover text
                ) )


fig.update_layout(
    title = "Cases vs Deaths per Major County in Texas",
    autosize=False,
    width=800,          # this is the size the graph will actually take up,
    barmode = 'stack',   #   can be removed to show so plotly fits automaticaly
)
fig.show()

#'''
#region
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig,
    style={'overflowY': 'scroll', 'width': 800},        # this line sets the scroll bar, 
    )                                                   #  couldnt find way to implement with just plotly
])                                                      # Note: width refers to what the container shows
app.run_server(debug=False, use_reloader=False)
#endregion
#'''
