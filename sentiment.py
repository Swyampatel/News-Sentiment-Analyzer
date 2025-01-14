import pandas as pd
from textblob import TextBlob

def analyze_sentiment(input_file, output_file):
    # Load the scraped data
    df = pd.read_csv(input_file)
    sentiments = []
    
    for title in df['title']:
        analysis = TextBlob(title)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        sentiments.append(sentiment)

    # Add sentiment to the dataframe
    df['sentiment'] = sentiments
    df.to_csv(output_file, index=False)
    print(f"Sentiment analysis saved to '{output_file}'.")

if __name__ == "__main__":
    analyze_sentiment("news_headlines.csv", "news_with_sentiment.csv")
