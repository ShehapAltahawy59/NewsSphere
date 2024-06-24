from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from flask_login import login_required, current_user
from requests import get
from models import db
from models import Article

main = Blueprint('main', __name__)

key = "8650af4fe36f411694acf596dbc3b72e"
url = "https://newsapi.org/v2/top-headlines?country=eg&"
business_response = get(url+"category=business&apiKey={}".format(key)).json()
health_response = get(url+"category=health&apiKey={}".format(key)).json()
general_response = get(url+"category=general&apiKey={}".format(key)).json()
sports_response = get(url+"category=sports&apiKey={}".format(key)).json()
technology_response = get(url+"category=technology&apiKey={}".format(key)).json()
with main.app_context():
    db.create_all()

@main.route("/")
def landing_page():
    

    return (render_template("landing_page.html",general_response = general_response))

@main.route('/Business')
def business():
    # Here you can add any logic to fetch and process data related to the Business category
    # For now, let's just render a template to display the Business category
    # You can pass any necessary data to the template as needed
    return render_template('landing_page.html',general_response= business_response)

@main.route('/Health')
def Health():
    # Here you can add any logic to fetch and process data related to the Business category
    # For now, let's just render a template to display the Business category
    # You can pass any necessary data to the template as needed
    return render_template('landing_page.html',general_response= health_response)

@main.route('/Sports')
def Sports():
    # Here you can add any logic to fetch and process data related to the Business category
    # For now, let's just render a template to display the Business category
    # You can pass any necessary data to the template as needed
    return render_template('landing_page.html',general_response= sports_response)

@main.route('/Technology')
def Technology():
    # Here you can add any logic to fetch and process data related to the Business category
    # For now, let's just render a template to display the Business category
    # You can pass any necessary data to the template as needed
    return render_template('landing_page.html',general_response= technology_response)

@main.route('/about')
def about_me():
    # Here you can add any logic to fetch and process data related to the Business category
    # For now, let's just render a template to display the Business category
    # You can pass any necessary data to the template as needed
    return render_template('about_me.html')

@main.route('/sources')
def sources():
    # Here you can add any logic to fetch and process data related to the Business category
    # For now, let's just render a template to display the Business category
    # You can pass any necessary data to the template as needed
    return render_template('sources.html')

@main.route('/search')
def search():
    query = request.args.get('query')
    response = get("https://newsapi.org/v2/everything?q={}&apiKey={}".format(query,key)).json()
    print(response)
    # You can pass any necessary data to the template as needed
    return render_template('landing_page.html',general_response = response)


@main.route('/add_article', methods=['GET', 'POST'])
@login_required
def add_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']
        publishing_date = datetime.strptime(request.form['publishing_date'], '%Y-%m-%d').date()
        publisher = request.form['publisher'] or 'NewsSphere'

        new_article = Article(title=title, content=content, category=category,
                              publishing_date=publishing_date, publisher=publisher,
                              user_id=current_user.id)
        db.session.add(new_article)
        db.session.commit()

        return redirect(url_for('landing_page'))

    return render_template('add_article.html')
