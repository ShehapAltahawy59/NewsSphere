from flask import Flask,render_template
from requests import get
app = Flask(__name__)
key = "8650af4fe36f411694acf596dbc3b72e"
url = "https://newsapi.org/v2/top-headlines?country=eg&"
business_response = get(url+"category=business&apiKey={}".format(key)).json()
health_response = get(url+"category=health&apiKey={}".format(key)).json()
general_response = get(url+"category=general&apiKey={}".format(key)).json()
sports_response = get(url+"category=sports&apiKey={}".format(key)).json()
technology_response = get(url+"category=technology&apiKey={}".format(key)).json()
@app.route("/")
def landing_page():
    

    return (render_template("landing_page.html",general_response = general_response))

@app.route('/Business')
def business():
    # Here you can add any logic to fetch and process data related to the Business category
    # For now, let's just render a template to display the Business category
    # You can pass any necessary data to the template as needed
    return render_template('landing_page.html',general_response= business_response)

@app.route('/Health')
def Health():
    # Here you can add any logic to fetch and process data related to the Business category
    # For now, let's just render a template to display the Business category
    # You can pass any necessary data to the template as needed
    return render_template('landing_page.html',general_response= health_response)

@app.route('/Sports')
def Sports():
    # Here you can add any logic to fetch and process data related to the Business category
    # For now, let's just render a template to display the Business category
    # You can pass any necessary data to the template as needed
    return render_template('landing_page.html',general_response= sports_response)

@app.route('/Technology')
def Technology():
    # Here you can add any logic to fetch and process data related to the Business category
    # For now, let's just render a template to display the Business category
    # You can pass any necessary data to the template as needed
    return render_template('landing_page.html',general_response= technology_response)

@app.route('/about_me')
def about_me():
    # Here you can add any logic to fetch and process data related to the Business category
    # For now, let's just render a template to display the Business category
    # You can pass any necessary data to the template as needed
    return render_template('about_me.html')

@app.route('/sources')
def sources():
    # Here you can add any logic to fetch and process data related to the Business category
    # For now, let's just render a template to display the Business category
    # You can pass any necessary data to the template as needed
    return render_template('sources.html')


if __name__ == "__main__":
    app.run(debug=True)
