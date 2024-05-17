import os
from flask import Flask, request, jsonify
from google.cloud import language_v1

app = Flask(__name__)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service-account-file.json"

def analyze_sentiment(text):
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
    return sentiment.score

@app.route('/analyze-sentiment', methods=['POST'])
def analyze_sentiment_endpoint():
    data = request.get_json()
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    score = analyze_sentiment(text)
    sentiment = 'Positive' if score > 0 else 'Negative'
    return jsonify({'sentiment': sentiment})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)