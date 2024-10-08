from . import db
from flask_login import UserMixin
from sql_alchey.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)    
    