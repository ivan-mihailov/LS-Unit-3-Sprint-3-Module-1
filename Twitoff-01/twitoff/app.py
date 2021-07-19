import os
from flask import Flask, render_template, request
from .models import db, User

def create_app():
    """Create and configure an instance of the Flask appication."""
    app_dir = os.path.dirname(os.path.abspath(__file__))
    database = "sqlite:///{}".format(os.path.join(app_dir, "twitoff.sqlite3"))
    
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = database
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    
    @app.route('/', methods=["GET", "POST"])
    def home():
        if request.form:
            print(request.form)
        return render_template("home.html")
    
    return app