from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/", methods=["POST"])
def analyze_sentiment():
    if request.method == "POST":
        try:
            data = request.get_json()
            text = data["text"] 
            sentiment = TextBlob(text).sentiment.polarity

            if sentiment > 0:
                result = "Positive"
            elif sentiment < 0:
                result = "Negative"
            else:
                result = "Neutral"

            return result
        except KeyError:
            return "Error: 'text' key not found in request data", 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
    #