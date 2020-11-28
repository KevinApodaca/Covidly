# Meeting Records 10/16/2020

- Attendees: Kevin, Jacob, Stephanie, Xavier, Sebastian, Richard, Antonio, Cynthia, Gilbert
- Start Time: 5:00pm
- End Time: 6:00pm

#### Summary:
We went over the slideshow for our initial presentation. Began discussing future subgroups that members would like to work on. We also assigned different slides to members to complete.

#### Member overview.
1. Kevin Apodaca 
  - Working on slide #3 of the powerpoint and the UI prototype.
2. Jacob Barberena
  - Working on slide #8 of the powerpoint.
3. Stephanie Callejas
  - Working on slide #8 of the powerpoint.
4. Valeria Gonzalez Muñoz
  - Working on slide #2 and UI prototype.
5. Xavier Martinez
  - Working on slide #8 of the powerpoint
6. Sebastian Nuñez
  - Working on slide #3 of the powerpoint and the UI prototype.
7. Richard Quinn
  - Working on slide #4 of the powerpoint.
8. Antonio Sosa
  - Working on slide #5, #2 of the powerpoint.
9. Cynthia Sustaita
  - Working on slide #5 of the powerpoint.
10. Gilbert Velasquez
  - Working on slide #4 of the powerpoint.

# Meeting Records 10/23/2020

- Attendees: Kevin, Jacob, Stephanie, Xavier, Sebastian, Richard, Antonio, Cynthia
- Start Time: 5:00pm
- End Time: 6:00pm

#### Summary:
We finalized UI design, completed most of the slides for presentation, discussed APIs and data sources for project.

# Meeting Records 10/30/2020
1. Antonio Sosa
  - Working on mapping functionality, pie charts and data visualizations. Working version of maps to demo. Investigation on other resources for El-Paso focused component of our project.
  
2. Gilbert Velasquez
  - API integrations with API team, investigation on visualization and user interaction components through Dash and Plotly. Working with Antonio
 
3. Jacob Barberena
  - Learning plotly with dash, creating charts and visualization components.
 
4. Richard Quinn
  - Learning HTML+CSS to help with front end component. Will look into Django.
  
5. Cynthia Sustaita, Valeria, Xavier, Sebastian, Gilbert
  - Working with API team, found replacements for aviationstack. Implemented and tested new API calls to make the project easier to track.
  - https://doc.aerodatabox.com/#operation/SearchAirportsByLocation, https://documenter.getpostman.com/view/8854915/SzS7NkEt?version=latest#99257d36-4e3e-40fb-9c31-8706d6a361c4, https://newsapi.org/docs/client-libraries/python, https://api.covidtracking.com/v1/states/tx/daily.json
 
6. Stephanie
  - Famliarized with Django, learning new framework.

7. Kevin
  - Worked on front end, have working version with map component and a bar chart.
  
#### Summary:
Discussed status update, new tools to replace old APIs, demo UI and the map components.

--- 
# Meeting Records 11/06/2020

- Attendees: Jacob, Stephanie, Xavier, Sebastian, Antonio, Cynthia, Gilbert
- Start Time: 5:00pm
- End Time: 6:00pm

#### Member overview.
1. Antonio Sosa
  - Working on visualization and interaction (pycharts)
  
2. Gilbert Velasquez
  - Icon for project (Prototypes up for demo - team discussion on team's discord). Researching plotly.
 
3. Jacob Barberena
  - Working on bargraph representing top 10 countries/cities (Will retrieve from API) 
 
4. Richard Quinn
  - Working on the flight tracker page - setting up
  
5. Cynthia Sustaita, Valeria, Xavier, Sebastian
  - NewsAPI: Need to modify query to obtain desired response. Data retrieval complete.
  - CovidAPI: Working on data retrieval.
  - TwitterAPI: Data retrieval complete, filtering desired fields. 
  - FlightsAPI: Arrival and departure need to be managed differently, working on the data retrieval. Had to research for new API.
  http://api.aviationstack.com/v1/flights?access_key=29a2ab9c0a0625c6a59aaa327eb291d7&arr_iata=ELP
 
6. Stephanie
  - Working on the flight tracker page

7. Kevin
- Finished layout of newsfeed page. Started presentation slides structure for Monday's (11/09) presentation
  
#### Summary:
Discussed individual updates. Discussing presentation set up.

---
# Meeting Records 11/13/2020

- Attendees: Jacob, Stephanie, Xavier, Sebastian, Cynthia, Gilbert
- Start Time: 5:00pm
- End Time: 6:00pm

#### Member overview.
1. Antonio Sosa
 - Created more visuals using plotly and retrieved data from the internet using BeautifulSoup.
  
2. Gilbert Velasquez
  - Developed scatterplot with plotly, shows deaths per country. Needs MR from Valeria to add new data and functionality. Meet with Jacob to work on `Trello-20`.
 
3. Jacob Barberena
  - Finished up `Trello-24` to develop the mirrored bar graph. Needs to get the data from API to show the latest data instead of hardcode.
 
4. Richard Quinn
  - Worked on flight tracker page. Will work with Stephanie to finish the frontend view for flight tracker.
  
5. Cynthia Sustaita
  - Finished `Trello-13` to retrieve news api, needs to separate into methods for frontend to better capture values.
  
6. Valeria
  - Finished python methods to get data for top 5 states in the U.S. 
  - Working on getting data about current hospitalized, and current in ICU
  - Working on getting cases by county from https://www.dshs.texas.gov/coronavirus/additionaldata/
  - Developed another version of the logo.
 
7. Xavier
  - Finished python implementation for `Trello-14` to get tweets.
  
8. Sebastian
  - Finished `Trello-15` to get the flight data for El Paso, Dallas, Austin, and San Antonio. Will work on extending this to include data from `Trello-24` to include more locations.
 
6. Stephanie
  - Catch up with Richard to finalize flight tracker page.

7. Kevin
  - Finished up `Trello-27` and `Trello-7`.

#### Summary:
Discussed individual updates. Discussed presentations for research articles. 

---
# Meeting Records 11/20/2020

- Attendees: Antonio, Gilbert, Jacob, Stephanie, Valeria, Xavier, Kevin
- Start Time: 5:00pm
- End Time: 6:00pm

#### Member overview.
1. Antonio
 - Investigate map not loading, working to add pie chart to frontend, coordinate with Jacob/ Gilbert to lend help with x-axis of data.
  
2. Gilbert & Jacob
  - Added new methods to retrieve data for grabbing monthly cases. Visualizations for monthly cases by state, having issues with visualization of data with X-Axis.
 
3. Richard Quinn, Stephanie
  - Fixed and display flight tracker page, working on cleaning up UI to match prototype. Added map component, stats data.
  
4. Valeria
  - Working on retreiving data file from state county cases for top 5 states through python. Fixed comments on git pull request. 
 
7. Xavier
  - Working on Embedding tweets on frontend newsfeed using Twitter developer docs. Will have a pull request up to test integration.

8. Kevin
  - Finished up `Trello-25`, `Trello-31`. Working on `Trello-31` and will fix issue with map not loading (`Trello-32`)

9. Cynthia & Sebastian
  - Working on adding data from news api into the frontend components
  - Reviewing merge requests
  
#### Summary:
Discussed individual updates. Agreed on new logo for project. Set plans to begin next interm status report project.

---

# Meeting Records 11/27/2020

- Attendees: Antonio, Gilbert, Jacob, Stephanie, Valeria, Xavier, Kevin
- Start Time: 5:00pm
- End Time: 6:00pm

#### Member overview.
1. Antonio
 - Working on two maps for displaying heatmaps, pie chart
  
2. Gilbert & Jacob, Antonio
  - Finalized scatterplot to display statistics for active cases for the top 5 states. Fixed date formatting issue. Added scrollbar to the mirror bar graph for reports.
 
3. Richard Quinn, Stephanie
  - Work with Cynthia, Sebastian to render newsfeed HTML into frontend,
  
4. Valeria
  - Finished up new logos for project. 
 
7. Xavier
  - Worked on embedding tweets, can render top 100 covid-related tweets to frontend newsfeed.

8. Kevin
  - Deployed covidly project to Heroku, finished `Trello-7`, working on `Trello-38` and `Trello-39` to fix small ui elements to newsfeed component.

9. Cynthia & Sebastian
  - Rework both the fetching of news data and the flights information to better adjust to frontend.
  - Display the newsfeed article, link url, and description on frontend. Need to make it dynamic to generate top 6 stories with efficient code.
  - Rendering
  - Can now render all 6 articles dynamically.
