<h1 align="center"> Covidly Project </h1> <br>
<h3> CS 4390 semester project as developed by Team 2 at the University of Texas at El Paso.</h3>

<p align="center">
  <img src="dashboard_illustration.svg" width=700>
</p>

## Project Structure
`core` contains frontend html files and static files.
`processdata/getdata.py` contains services for fetching data.
## Running Project
To run the project take the following steps
1. `git clone https://github.com/KevinApodaca/Covidly.git`
2. Run a virtual python environment with `python -m venv env`
3. Install the project dependencies with `pip3 install -r requirements.txt`
4. Run the migrations with `python manage.py makemigrations` and then run the command `python manage.py migrate`
5. Run the local development server with `python manage.py runserver` 

## Deploying Project
There was a mistake on title 
