from os import environ, path
from controllers.scores import Scores_Api
from controllers.cards import Cards_Create, Cards_Others
from controllers.decks import Decks_Create, Deck_Others
from controllers.cardsbydeck import AllCrds, GetAll
from models.score import Scores
# from models.card import Cards
from models.deck import Decks
from models.users import user_datastore
from models import db
from flask import Flask, render_template
from flask_security import Security, auth_required
from flask_restful import Api
from celeryConfig import add_together
from cacheConfig import cache

# Create app
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "super-secret"
app.config["SECURITY_PASSWORD_SALT"] = "HelloWorld"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.config["WTF_CSRF_ENABLED"] = False


# Create database connection object
db.init_app(app)
security = Security(app, user_datastore)

# Create Cache Object
cache.init_app(app)

# Create a user to test with
@app.before_first_request
def create_user():
    file_exists = path.exists("database.sqlite3")
    if file_exists != True:
        db.create_all()
        user_datastore.create_user(email="sachin@mail.com", password="root")
        user_datastore.create_user(email="user@mail.com", password="user")
        db.session.commit()


# Views
@app.route("/")
def HelloWorld():
    return "HelloWorld"

# Celery Routes.

@app.route("/celery")
def mockCel():
    add_together.delay(10,21)
    return "Hi"

@app.route("/daily")
def dailyJobs():
    # add_together.delay(10,21)
    return render_template("daily.html")

@app.route("/timed")
def timedJobs():
    # add_together.delay(10,21)
    return render_template("timed.html")


############# Export Url ###############

@app.route("/pdf")
@cache.cached(timeout=50)
def pdf():
    return GetAll()


@app.route("/app")
@auth_required("token")
def plot():
    return "Hello  World!!"


############### Core Views ##################


@app.route("/signin")
def signin():
    return render_template("login.html")


@app.route("/dashboard")
@cache.cached(timeout=50)
def index():
    return render_template("index.html")


@app.route("/create/deck")
def CreateDeck():
    return render_template("deck-form.html")


@app.route("/modify/deck")
def ModifyDeck():
    return render_template("decks.html")


@app.route("/cards/<deck_id>/<n>")
def Cards(deck_id, n):
    return render_template("cards.html", deck=deck_id, name=n)


@app.route("/review/<deck_id>/<n>")
def Review(deck_id, n):
    return render_template("review.html", deck=deck_id, name=n)


# Api Intialisation
api = Api(app)
api.add_resource(Decks_Create, "/api/deck")
api.add_resource(Deck_Others, "/api/deck/<deck_id>")
api.add_resource(Cards_Create, "/api/card")
api.add_resource(Cards_Others, "/api/card/<card_id>")
api.add_resource(Scores_Api, "/api/user/<u_id>/deck/<d_id>")
api.add_resource(AllCrds, "/api/cardsbydeck/<d_id>")

if __name__ == "__main__":
    app.run(port=environ.get("PORT", 8080), host="0.0.0.0", debug=True)
