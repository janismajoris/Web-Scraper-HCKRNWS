import requests
from bs4 import BeautifulSoup

#URLs

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")

articles_text = []
articles_link = []

articles = soup.find_all(name="span", class_="titleline")
for article_tag in articles:
    text = article_tag.get_text()
    articles_text.append(text)
    link = article_tag.find(name="a").get("href")
    articles_link.append(link)

article_scores = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(len(articles_text))
print(len(articles_link))
print(article_scores)
print(len(article_scores))


hckr_news_list = {}
for number in range(len(articles_text)):

    hckr_news_list[number] = {
        "text": articles_text[number],
        "link": articles_link[number],
        "score": article_scores[number-1],
    }

print(hckr_news_list)
