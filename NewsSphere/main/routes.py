from flask import render_template,request,Blueprint,url_for
import requests
from bs4 import BeautifulSoup
main  = Blueprint("main",__name__)


key = "40b6ad40eb474fd183802d736f63822f"
url = "https://newsapi.org/v2/top-headlines?country=eg&"
# business_response = get(url+"category=business&apiKey={}".format(key)).json()
# health_response = get(url+"category=health&apiKey={}".format(key)).json()
# general_response = get(url+"category=general&apiKey={}".format(key)).json()
# sports_response = get(url+"category=sports&apiKey={}".format(key)).json()
# technology_response = get(url+"category=technology&apiKey={}".format(key)).json()

# Function to fetch news articles

def check_image_url(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            return url
        else:
            return url_for('static', filename='News_featured.png')
    except requests.RequestException:
        return url_for('static', filename='News_featured.png')



def fetch_news(category, query=None, page=1, page_size=5):
    url = f"https://newsapi.org/v2/top-headlines?country=eg&category={category}&page={page}&pageSize={page_size}&apiKey={key}"
    if query:
        
        url = f"https://newsapi.org/v2/everything?q={query}&page={page}&pageSize={page_size}&apiKey={key}"
    response = requests.get(url).json()
    return response

@main.route("/")
def landing_page():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('pageSize', 10, type=int)
    general_response = fetch_news(category="general", page=page, page_size=page_size)
    total_results = general_response.get('totalResults', 0)
    for news in general_response['articles']:
        if news['urlToImage']:
            news['urlToImage'] = check_image_url(news['urlToImage'])
            
        else:
            news['urlToImage'] = url_for('static', filename='News_featured.png')
    return render_template("landing_page.html", general_response=general_response['articles'], current_page=page, page_size=page_size, total_results=total_results, category='general')

@main.route('/Business')
def business():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('pageSize', 10, type=int)
    business_response = fetch_news(category="business", page=page, page_size=page_size)
    total_results = business_response.get('totalResults', 0)
    for news in business_response['articles']:
        if news['urlToImage']:
            news['urlToImage'] = check_image_url(news['urlToImage'])
            
        else:
            news['urlToImage'] = url_for('static', filename='entrepreneur-1340649_1280.jpg')
    return render_template('landing_page.html', general_response=business_response['articles'], current_page=page, page_size=page_size, total_results=total_results, category='business')

@main.route('/Health')
def health():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('pageSize', 10, type=int)
    health_response = fetch_news(category="health", page=page, page_size=page_size)
    total_results = health_response.get('totalResults', 0)
    for news in health_response['articles']:
        if news['urlToImage']:
            news['urlToImage'] = check_image_url(news['urlToImage'])
            
        else:
            news['urlToImage'] = url_for('static', filename='blood-pressure-1584223_1280.jpg')
    return render_template('landing_page.html', general_response=health_response['articles'], current_page=page, page_size=page_size, total_results=total_results, category='health')

@main.route('/Sports')
def sports():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('pageSize', 10, type=int)
    sports_response = fetch_news(category="sports", page=page, page_size=page_size)
    total_results = sports_response.get('totalResults', 0)
    for news in sports_response['articles']:
        if news['urlToImage']:
            news['urlToImage'] = check_image_url(news['urlToImage'])
            
        else:
            news['urlToImage'] = url_for('static', filename='stadium-1590576_1280.jpg')
    return render_template('landing_page.html', general_response=sports_response['articles'], current_page=page, page_size=page_size, total_results=total_results, category='sports')

@main.route('/Technology')
def technology():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('pageSize', 10, type=int)
    technology_response = fetch_news(category="technology", page=page, page_size=page_size)
    total_results = technology_response.get('totalResults', 0)
    for news in technology_response['articles']:
        if news['urlToImage']:
            news['urlToImage'] = check_image_url(news['urlToImage'])
            
        else:
            news['urlToImage'] = url_for('static', filename='industry-3087393_1280.jpg')
    return render_template('landing_page.html', general_response=technology_response['articles'], current_page=page, page_size=page_size, total_results=total_results, category='technology')



@main.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    page = request.args.get('page', 1, type=int)  # Get the current page, default to 1
    page_size = request.args.get('pageSize', 10, type=int)  # Number of results per page, default to 10
    search_response =fetch_news(category=None,query=query,page=page,page_size=page_size)
    total_results = search_response.get('totalResults', 0)
    for news in search_response['articles']:
        if news['urlToImage']:
            news['urlToImage'] = check_image_url(news['urlToImage'])
            
        else:
            news['urlToImage'] = url_for('static', filename='News_featured.png')
    

    return render_template(
        'landing_page.html',
        general_response=search_response['articles'],
        query=query,
        current_page=page,
        page_size=page_size,
        total_results=total_results
    )


@main.route('/about')
def about_me():
    
    return render_template('about_me.html')

@main.route('/sources')
def sources():
   
    return render_template('sources.html')
