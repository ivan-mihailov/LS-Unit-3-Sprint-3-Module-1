from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Create a 'user' table
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True) # id as Primary Key
    name = db.Column(db.String(50), nullable = False) # user name

    def __repr__(self):
        return "<User: {}>".format(self.name)