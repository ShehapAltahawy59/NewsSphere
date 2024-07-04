from flask import Blueprint,request,redirect,url_for,render_template,jsonify
from flask_login import login_user,current_user,logout_user,login_required
from NewsSphere.users.forms import regestration,Login
from NewsSphere.models.Models import User,Saved_news
from NewsSphere import db,bcrypt
users = Blueprint('users',__name__)

@users.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.landing_page'))
    form = regestration()
    error = None
    if request.method == "POST":
        if (form.password.data != form.confirmed_password.data):
            error = "Passwords must match"
            
            return render_template('register.html', title = 'register',form =form,password_error=error)

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,password=hashed_password,email=form.email.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))

    return render_template('register.html', title = 'register',form =form,password_error=error)

@users.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.landing_page'))
    form = Login()
    error = None
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user=user,remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page :
                print(next_page)
                return redirect((next_page))
            return redirect(url_for('main.landing_page'))
        else:
            error="please check Email and Password "
    return render_template('login.html', title = 'login',form =form, error=error)

@users.route('/logout',methods=["POST","GET"])
def logout():
    logout_user()
    return redirect(url_for('main.landing_page'))

@users.route('/account')
@login_required
def account():
    return render_template('account.html')

@users.route('/save_news', methods=['POST'])
@login_required
def save_news():
    print("here")
    data = request.get_json()
    title = data['title']
    description = data.get('description', '')
    url = data['url']
    urlToImage = data['urlToImage']
    
    existing_news = Saved_news.query.filter_by(user_id=current_user.id, url=url).first()
    if existing_news:
        return jsonify(success=False, message='the news already saved.')

    new_news = Saved_news(title=title, description=description, url=url,urlToImage=urlToImage, user_id=current_user.id)
    db.session.add(new_news)
    db.session.commit()
    print("saved")
    return jsonify(success=True)


@users.route('/del_news', methods=['POST'])
@login_required
def del_news():
    print("here")
    data = request.get_json()
    url = data['url']
    
    existing_news = Saved_news.query.filter_by(user_id=current_user.id, url=url).first()

    if existing_news:
        db.session.delete(existing_news)
        db.session.commit()
        
        return jsonify(success=True)
    else:
        return jsonify(success=False, message='The news article does not exist.')


@users.route('/is_saved', methods=['GET'])
@login_required
def is_saved():
    url = request.args.get('url')

    saved_article = Saved_news.query.filter_by(user_id=current_user.id, url=url).first()
    is_saved = saved_article is not None

    return jsonify({'is_saved': is_saved})


@users.route('/Saved_News')
@login_required
def Saved_News():
    
    saved_news = Saved_news.query.filter_by(user_id=current_user.id)
    return render_template('saved_news.html',saved_news=saved_news)
