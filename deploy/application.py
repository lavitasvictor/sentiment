from flask import Flask, redirect, render_template, request, url_for
import sys
import helpers
from analyzer import Analyzer
from time import ctime
from cs50 import SQL
db = SQL("sqlite:///user_agents.db")


app = Flask(__name__)
@app.route("/")
def index():
    db.execute("INSERT INTO agent('user_agent','ip','current_time') VALUES(:user_agent, :ip, :current_time);", user_agent = request.headers.get('User-Agent'), ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr), current_time = ctime())
    return render_template("index.html")

@app.route('/registred')
def registred():
    return str(db.execute("SELECT * FROM agent;"))

@app.route("/search")
def search():
    # validate screen_name
    screen_name = request.args.get("screen_name", "").lstrip("@")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name, count = 100)

    # TODO-DONE
    #REDIRECT TO INDEX IF NONE
    if not tweets:
        return redirect(url_for("index"))
    #INITIALIZE ANALYZER
    positives = "/home/vbrn/deploy/positive-words.txt"
    negatives = "/home/vbrn/deploy/negative-words.txt"
    analyzer = Analyzer(positives, negatives)
    #ANALYZE tweets
    #1) ITERATE OVER TWEETS
    positive, negative, neutral = 0.0, 0.0, 0.0
    for tweet in tweets:
        #2) SCORE WORDS IN TWEET
        score=analyzer.analyze(tweet)
        #3) KEEP TRACK OF WHETHER TWEET IS POSITIVE, NEGATIVE OR NEUTRAL
        if score > 0:
            positive +=10
        elif score < 0:
            negative +=10
        else:
            neutral +=10


    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)

app.debug = True

