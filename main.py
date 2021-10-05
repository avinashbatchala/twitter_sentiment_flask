from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

access_token = "4824134823-0RmJm6xrG905UVP6CIsQ0kvTISasUVkImv7TR6O"
access_token_secret = "VCqgnYiDPF6elHcnbRGJRiTGs3Vo3TiEKXcoM4G2oWMIS"
consumer_key = "RMPUEZXZcYTe0UzIhCqJ7hVDy"
consumer_secret = "Or5j6mnXcIOKVLeF5aHBpkecfFIdmvivoLdX3SaiJK3ptJYLwX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})

app.run()