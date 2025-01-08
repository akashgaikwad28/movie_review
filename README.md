# Movie Review Sentiment Analyzer

A simple Flask web application that analyzes the sentiment of movie reviews using TextBlob. The application provides instant feedback on whether a review is positive, negative, or neutral, along with a polarity score.

## Features

- Real-time sentiment analysis of movie reviews
- Clean and responsive web interface
- Displays both sentiment category and polarity score
- Color-coded results for easy interpretation
- No database required - instant analysis

## Prerequisites

Before running this application, make sure you have the following installed:
- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the files:
```bash
git clone <repository-url>
# or create a new directory and copy the files manually
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Unix or MacOS
python -m venv venv
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install flask textblob
```

4. Directory structure should look like this:
```
movie_review_app/
├── app.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── README.md
```

## Running the Application

1. Make sure your virtual environment is activated

2. Run the Flask application:
```bash
python app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Enter a movie review in the text area
2. Click the "Analyze Review" button
3. View the analysis results:
   - Sentiment (Positive, Negative, or Neutral)
   - Polarity Score (-1 to 1)
   - Color-coded result card for quick interpretation

## Technology Stack

- **Flask**: Web framework
- **TextBlob**: Natural Language Processing library for sentiment analysis
- **HTML/CSS**: Frontend interface
- **Python**: Backend logic

## File Structure

- `app.py`: Main application file containing Flask routes and sentiment analysis logic
- `templates/index.html`: HTML template for the web interface
- `static/style.css`: CSS styles for the application

## How It Works

The application uses TextBlob's sentiment analysis to process movie reviews. The sentiment analysis returns two main components:
- **Polarity**: A float value between -1 and 1, where:
  - 1 means positive sentiment
  - 0 means neutral sentiment
  - -1 means negative sentiment
- **Classification**: Based on the polarity score, the review is classified as:
  - Positive (polarity > 0)
  - Neutral (polarity = 0)
  - Negative (polarity < 0)

