from . import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    publishing_date = db.Column(db.Date, nullable=False)
    publisher = db.Column(db.String(100), nullable=False, default='NewsSphere')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f'<Article {self.title}>'
