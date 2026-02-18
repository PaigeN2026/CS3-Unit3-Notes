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
    favorites_list = ['27 Dresses', 'Bride Wars', '50 First Dates', 'How To Lose A Guy In 10 Days', 'Pretty Woman', 'The Proposal', '10 Things I Hate About You']
    ratings_dict = { 
                    "27 Dresses" : "boo bleh", 
                    "Bride Wars" : "",
                    "50 First Dates" : "",
                    "How To Lose A Guy In 10 Days" : "",
                    "Pretty Woman" : "",
                    "The Proposal" : "",
                    "10 Things I Hate About you" : ""
                    }
    return render_template("index.html", name=name_data, year=year_data, favorites=favorites_list, ratings=ratings_dict)

# TO RUN YOUR APP enter "flask run" into the TERMINAL
# TO STOP click CTRL + C in the TERMINAL 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)