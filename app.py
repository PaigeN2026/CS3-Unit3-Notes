from flask import Flask
from flask import render_template

# Create an instance of Flask
app = Flask(__name__)

# Function that returns content
# using the app.route decorator to map the URL
@app.route("/")
def index(): 
    # Pass variables from Python to HTML
    name_data = 'Paige'
    year_data = 2026
    # Can also use lists & dictionaries 
    favorites_list = ['Jo', 'Wo', 'No', 'Ko']
    ratings_dict = { 
                    'Jo' : 3, 
                    'Wo' : 5,
                    'No' : 9,
                    'Ko' : 1
                    }
    return render_template("index.html", name=name_data, year=year_data, favorites=favorites_list, ratings=ratings_dict)

# TO RUN YOUR APP enter "flask run" into the TERMINAL
# TO STOP click CTRL + C in the TERMINAL 