import urllib.request
from bs4 import BeautifulSoup

'''
urllib.error.URLError:
SSL認証エラー発生
macOSが原因
https://qiita.com/orangain/items/0a641d980019fd7e0c52

'''


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        response = urllib.request.urlopen(self.site)
        html = response.read()
        parser = "html.parser"
        soup = BeautifulSoup(html, parser)

        with open("news_headline.txt", "w") as file:
            for tag in soup.find_all("a"):
                url = tag.get("href")
                # 日本語のニュースページにはhtmlを含むhref属性がない
                if url and  "articles" in url:
                    file.write("/n" + url)
        print("file save end")

news = "https://news.google.com/"
Scraper(news).scrape()
