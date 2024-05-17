from flask import Flask, request
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("https://be-cloud-computing-course-project.rahtiapp.fi/", methods=["GET", "POST"])
def analyze_sentiment():
  if request.method == "POST":
    text = request.form["text"] 
    sentiment = TextBlob(text).sentiment.polarity

    if sentiment > 0:
      result = "Positive"
    elif sentiment < 0:
      result = "Negative"
    else:
      result = "Neutral"

    return result
  else:
    return "<p>Enter text for sentiment analysis</p><form method='POST'><input type='text' name='text' /><input type='submit' value='Analyze'></form>"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)