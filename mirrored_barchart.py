import plotly
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html


    # -- save city displyed in reverse order on actual chart, save in reverse order to show correctly
cities = ['Houston','San Antonio','Dallas', 'Austin', 'Fort Worth', 
    'El Paso', 'Arlington', 'Corpus Cristi', 'Plano', 'Laredo']


    # -- implement API calls to avoid hard code data
cases = [100, 200, 300, 400, 420, 500, 600, 700, 800, 850]
deaths = [25, 50,  75,  130, 350, 250, 300, 215, 612, 667]

neg_deaths = []

for i in range(len(deaths)):
    neg_deaths.append( deaths[i]*-1 )

fig = go.Figure()

    # -- change hover over data, change color to fit project theme
fig.add_trace(go.Bar(x=cases, y=cities,
                base=0,
                marker_color='lightgreen',
                name='cases',
                orientation='h'
                ))
fig.add_trace(go.Bar(x=deaths, y=cities,
                base=neg_deaths,
                marker_color='lightslategrey',
                name='deaths',
                orientation='h'
                ))

fig.update_layout(
    autosize=False,
    width=800,          #can change dimensions depending on requirement
    height=450,
    barmode = 'stack'
)

'''
#region
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])
app.run_server(debug=False, use_reloader=False)
#endregion
'''

