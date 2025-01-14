import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def visualize_data(input_file):
    # Load the analyzed data
    df = pd.read_csv(input_file)

    # Plot Sentiment Distribution
    sentiment_counts = df['sentiment'].value_counts()
    sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'])
    plt.title("Sentiment Distribution of News Headlines")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.show()

    # Generate Word Cloud
    text = " ".join(df['title'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Word Cloud of News Headlines")
    plt.show()

if __name__ == "__main__":
    visualize_data("news_with_sentiment.csv")
