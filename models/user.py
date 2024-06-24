from . import db
import bcrypt


class User(db.Model):
    """
    Represents a user in the application.
    Attributes:
    id (int): The unique identifier for the user.
    username (str): The username for the user, which must be unique.
    email (str): The email address for the user, which must be unique.
    password (str): The hashed password for the user.
    preferences (str): The user's preferences, stored as a string.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    preferences = db.Column(db.String(200))
    is_active = db.Column(db.Boolean, default=True)

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
