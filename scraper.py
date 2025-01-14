import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_news():
    url = "https://www.bbc.com/news"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to fetch the webpage.")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    news_data = []
    headlines = soup.find_all('h2', {'data-testid': 'card-headline'})
    for headline in headlines:
        title = headline.text.strip()
        news_data.append({"title": title})

    return news_data

if __name__ == "__main__":
    news = scrape_news()
    if not news:
        print("No news articles were scraped.")
    else:
        # Save the data to a CSV file
        df = pd.DataFrame(news)
        df.to_csv("news_headlines.csv", index=False)
        print("News headlines saved to 'news_headlines.csv'.")
