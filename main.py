import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class HackerNewsScraper:
    """A scraper for Hacker News articles."""

    BASE_URL = "https://news.ycombinator.com/"

    def __init__(self):
        """Initialize the scraper with a requests session."""
        self.session = requests.Session()
        self.session.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    def get_top_articles(self):
        """Fetch top articles from Hacker News."""
        try:
            response = self.session.get(self.BASE_URL)
            response.raise_for_status()  # Raises a HTTPError if the response status code is 4XX/5XX
            soup = BeautifulSoup(response.text, "html.parser")
            return self._parse_articles(soup)
        except requests.RequestException as e:
            logging.error(f"Error fetching articles: {e}")
            return []

    def _parse_articles(self, soup):
        """Parse articles from the BeautifulSoup object."""
        articles = []
        titles = soup.find_all("a", class_="titlelink")
        scores = {score.parent.attrs["id"]: int(score.text.split()[0]) for score in soup.find_all("span", class_="score")}

        for title in titles:
            item_id = title.parent.parent.attrs["id"]
            score = scores.get(f"score_{item_id}", 0)  # Default score to 0 if not found
            articles.append({
                "title": title.text,
                "link": urljoin(self.BASE_URL, title.get("href")),
                "score": score,
            })

        return articles

if __name__ == "__main__":
    scraper = HackerNewsScraper()
    top_articles = scraper.get_top_articles()

    for article in top_articles:
        print(f"Title: {article['title']}, Link: {article['link']}, Score: {article['score']}")
