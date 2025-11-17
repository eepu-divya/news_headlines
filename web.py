import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                      'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                      'Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return []

    print(f"Response status code: {response.status_code}")  # Debug info
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    # Example: scraping first 10 headlines from Hacker News
    stories = soup.select('a.storylink')
    for story in stories[:10]:
        headline = story.get_text(strip=True)
        if headline:
            headlines.append(headline)

    return headlines

def save_headlines(headlines, filename='headlines.txt'):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for headline in headlines:
                f.write(headline + '\n')
        print(f"Saved {len(headlines)} headlines to {filename}")
    except IOError as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    news_url = "https://news.ycombinator.com/"
    headlines = fetch_headlines(news_url)
    if headlines:
        save_headlines(headlines)
    else:
        print("No headlines found or error occurred during scraping.")
