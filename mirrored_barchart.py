from apis import covid_daily_api
import plotly
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html

texas_counties = ['Harris', 'Dallas', 'Tarrant', 'Bexar', 'Travis', 'Collin', 'Denton', 'Hidalgo', 'El Paso', 'Fort Bend']

allCountiesCases = []
for county in texas_counties:
    county_cases = covid_daily_api.casesCounty(county, "Texas")
    allCountiesCases.append(county_cases)

allCountiesDeaths = []
for county in texas_counties:
    county_death = covid_daily_api.deathsCounty(county, "Texas")
    allCountiesDeaths.append(county_death)

cases = allCountiesCases

#deaths = allCountiesDeaths                  # needs to strip trailing zeros

deaths = []
for num in allCountiesDeaths:
    deaths.append( int(num) )

neg_deaths = []

for i in range(len(deaths)):
    neg_deaths.append( deaths[i]*-1 )

fig = go.Figure()

fig.add_trace(go.Bar(x=cases[::-1], y=texas_counties[::-1],
                base=0,
                marker_color='orange',
                name='Cases',
                orientation='h',
                text = cases[::-1],
                textposition = 'inside',
                insidetextanchor = 'start',
                hovertemplate = 
                    'County: %{y}'+
                    '<br></b>Cases:</b> %{text} </br><extra></extra>', 
                ) 
            )

fig.add_trace(go.Bar(x=neg_deaths[::-1], y=texas_counties[::-1],
                base=0,
                marker_color='crimson',
                name='Deaths',
                orientation='h',
                text = deaths[::-1],
                textposition = 'outside',
                insidetextanchor = 'start',
                hovertemplate =
                    'County: %{y}'+
                    '<br></b>Deaths:</b> %{text} </br><extra></extra>',
                )
            )


fig.update_layout(
    title = "Cases against Deaths per Major County in Texas",
    autosize=False,
    width=1500,          # this is the size the graph will actually take up, can be removed to show so plotly fits automaticaly
    barmode = 'stack',
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="left",
        x=0)
)
#fig.show()

mirroredBarChart = dash.Dash()
mirroredBarChart.layout = html.Div([
    dcc.Graph(figure=fig,
    style={'overflowY': 'scroll', 'width': 600},        # this line sets the scroll bar, 
    )                                                   # Note: width refers to what the container shows
])

mirroredBarChart.run_server(debug=False, use_reloader=False)                 #remove this to place into website
