from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = ""
    comment = ""
    if request.method == "POST":
        comment = request.form["comment"]
        sentiment = analyze_sentiment(comment)
        print(f"Received comment: {comment} — Sentiment: {sentiment}")  # Debug print
    return render_template("index.html", sentiment=sentiment, comment=comment)

if __name__ == "__main__":
    app.run(debug=True)
