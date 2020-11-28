import plotly
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html


#   IMPORTANT NOTE: 
#     I used Sourcerree to merge 'Trelo-12-covidAPI' into 'Trello-24-mirrored_barchart' to get the updated covi_daily_api.py file 
#     before having the full merge pull request was approved, not sure if this would affect stuff


citiesArr = ['Houston','San Antonio','Dallas', 'Austin', 'Fort Worth', 
    'El Paso', 'Arlington', 'Corpus Cristi', 'Plano', 'Laredo']

#       For Sebastian's Flight Data: 
#arlington and plano not supported
# Lubbock and amarillo are good


#use Valeria's NY cities data

    # -- implement API calls to avoid hard code data
cases = [3270, 2400, 1200, 1400, 2420, 3000, 900, 700, 800, 1000]
deaths = [320, 230,  455,  830, 350, 350, 300, 215, 610, 665]

    # -- loop ready for API call implemetation (assuming data returns a single number), just need to set: cases, deaths = []
#for city in citiesArr:
#    cases.append( getdata.usa_cityCases(city) )
#    deaths.append( getdata.usa_cityDeaths(city) )

neg_deaths = []

for i in range(len(deaths)):
    neg_deaths.append( deaths[i]*-1 )

fig = go.Figure()

fig.add_trace(go.Bar(x=cases[::-1], y=citiesArr[::-1],
                base=0,
                marker_color='orange',
                name='Cases',
                orientation='h',
                text = cases[::-1],
                textposition = 'inside',
                insidetextanchor = 'start',
                hoverinfo = 'y',                #change to 'none' to disable bar hover text
                ) )
fig.add_trace(go.Bar(x=neg_deaths[::-1], y=citiesArr[::-1],
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
    title = "Cases vs Deaths per Major City in Texas",
    autosize=False,
    width=800,          # this is the size the graph will actually take up,
    barmode = 'stack',   #   can be removed to show so plotly fits automaticaly
)
#fig.show()

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
