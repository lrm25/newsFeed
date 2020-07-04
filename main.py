import urllib.request

from bs4 import BeautifulSoup

def main():
    with urllib.request.urlopen('http://public.nrao.edu/news') as response:
        data = response.read()
        data_soup = BeautifulSoup(data, 'html.parser')
        all_news = data_soup.find("div", class_="all-news")
        news_rows = all_news.find_all("div", class_="row")
        for news_row in news_rows:
            meta = news_row.find("div", class_="news-list-meta")
            date_and_time = meta.text.split('|')
            print(date_and_time[0])
            headline = news_row.find("div", class_="news-list-title")
            print(headline.text)

    with urllib.request.urlopen('https://www.eso.org/public/news') as response:
        data = response.read()
        print(data)

if __name__ == "__main__":
    main()
