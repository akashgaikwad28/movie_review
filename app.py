from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    analysis = TextBlob(text)
    # Get polarity score (-1 to 1)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        return 'Positive', polarity
    elif polarity < 0:
        return 'Negative', polarity
    else:
        return 'Neutral', polarity

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    review_text = None
    polarity = None
    
    if request.method == 'POST':
        review_text = request.form.get('review')
        if review_text:
            sentiment, polarity = analyze_sentiment(review_text)
            result = sentiment
            polarity = round(polarity, 2)
    
    return render_template('index.html', result=result, review=review_text, polarity=polarity)

if __name__ == '__main__':
    app.run(debug=True)