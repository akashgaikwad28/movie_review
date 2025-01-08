# app.py (main Streamlit file)
import streamlit as st
from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        return 'Positive', polarity
    elif polarity < 0:
        return 'Negative', polarity
    else:
        return 'Neutral', polarity

st.title('Movie Review Analyzer')

# Create a text area for the review
review_text = st.text_area('Enter your movie review:', height=150)

# Create an analyze button
if st.button('Analyze Review'):
    if review_text:
        sentiment, polarity = analyze_sentiment(review_text)
        
        # Create columns for better layout
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader('Sentiment')
            if sentiment == 'Positive':
                st.success(sentiment)
            elif sentiment == 'Negative':
                st.error(sentiment)
            else:
                st.info(sentiment)
                
        with col2:
            st.subheader('Polarity Score')
            st.write(f"{polarity:.2f}")
            
        # Show the analyzed text
        st.subheader('Your Review')
        st.write(review_text)
    else:
        st.warning('Please enter a review to analyze.')

# Add a footer with information
st.markdown('---')
st.markdown('Made with TextBlob for sentiment analysis')
