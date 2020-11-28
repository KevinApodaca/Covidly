from apis import covid_daily_api
import plotly.express as px
import pandas
from datetime import datetime
import plotly.graph_objects as go
from plotly.offline import plot

TXCases, TXDates = covid_daily_api.getMonthlyCases("texas")
CACases, CADates = covid_daily_api.getMonthlyCases("california")
NYCases, NYDates = covid_daily_api.getMonthlyCases("new york")
UTCases, UTDates = covid_daily_api.getMonthlyCases("utah")
FLCases, FLDates = covid_daily_api.getMonthlyCases("florida")

# This Method is used to modify the date attribute that will be used for our X - axis  mm/dd/yy
def fixAxis():
    for i in range(len(TXDates)):
        monthStr =str(TXDates[i])[:2]
        dayStr = str(TXDates[i] % 100)
        result = (monthStr + "/" + dayStr + "/20")
        TXDates[i] = result

        monthStr =str(CADates[i])[:2]
        dayStr = str(CADates[i] % 100)
        result = (monthStr + "/" + dayStr + "/20")
        CADates[i] = result

        monthStr =str(NYDates[i])[:2]
        dayStr = str(NYDates[i] % 100)
        result = (monthStr + "/" + dayStr + "/20")
        NYDates[i] = result

        monthStr =str(UTDates[i])[:2]
        dayStr = str(UTDates[i] % 100)
        result = (monthStr + "/" + dayStr + "/20")
        UTDates[i] = result

        monthStr =str(FLDates[i])[:2]
        dayStr = str(FLDates[i] % 100)
        result = (monthStr + "/" + dayStr + "/20")
        FLDates[i] = result


# This Method is used to create the Figure containing the 6 different Scatterplots
def createFigure():


    day = (int(datetime.today().strftime("%d")) - 1)
    fixAxis()

    StateGraph = go.Figure()
    StateGraph.add_trace(go.Scatter(x = TXDates[::-1], y = TXCases[::-1], mode = "lines+markers", name = "Texas", visible= True, line= dict(color = "red"))) # Texas
    StateGraph.add_trace(go.Scatter(x = CADates[::-1], y = CACases[::-1], mode = "lines+markers", name = "California", visible = False, line= dict(color = "blue"))) # California
    StateGraph.add_trace(go.Scatter(x = NYDates[::-1], y = NYCases[::-1], mode = "lines+markers", name = "New York", visible = False, line= dict(color = "orange"))) # New York
    StateGraph.add_trace(go.Scatter(x = UTDates[::-1], y = UTCases[::-1], mode = "lines+markers", name = "Utah", visible = False, line= dict(color = "purple"))) # Utah
    StateGraph.add_trace(go.Scatter(x = FLDates[::-1], y = FLCases[::-1], mode = "lines+markers", name = "Florida", visible = False, line= dict(color = "green"))) # Florida

    StateGraph.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="right",
                active=0,
                x=0.57,
                y=1.2,
                buttons=list([
                    dict(label="Texas",
                         method="update",
                         args=[{"visible": [True,False,False,False,False]},
                               {"title": "Texas Active Cases",
                                "annotations": []}]),
                    dict(label="California",
                         method="update",
                         args=[{"visible": [False,True,False,False,False]},
                               {"title": "California Active Cases",
                                "annotations": []}]),
                    dict(label="New York",
                         method="update",
                         args=[{"visible":[False,False,True,False,False]},
                               {"title": "New York Active Cases",
                                "annotations": []}]),
                    dict(label="Utah",
                         method="update",
                         args=[{"visible": [False,False,False,True,False] },
                               {"title": "Utah Active Cases",
                                "annotations": []}]),
                    dict(label="Florida",
                         method="update",
                         args=[{"visible":[False,False,False,False,True] },
                               {"title": "Florida Active Cases",
                                "annotations": []}]),
                    dict(label="All",
                         method="update",
                         args=[{"visible":[True,True,True,True,True]},
                               {"title": "States Active Cases",
                                "annotations": []}]),
                ]),
            )
        ])
    return StateGraph


plot(createFigure())