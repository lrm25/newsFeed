import urllib.request

from bs4 import BeautifulSoup

nrao_url = 'http://public.nrao.edu/news'

def response_read_func(response):
    return response.read()

def parse_nrao(url):
    response = urllib.request.urlopen(url)
    data = response_read_func(response)
    if data == None:
        raise ValueError("No data returned")
    data_soup = BeautifulSoup(data, 'html.parser')
    all_news = data_soup.find("div", class_="all-news")
    news_rows = all_news.find_all("div", class_="row")
    for news_row in news_rows:
        meta = news_row.find("div", class_="news-list-meta")
        date_and_time = meta.text.split('|')
        print(date_and_time[0])
        headline = news_row.find("div", class_="news-list-title")
        print(headline.text)

def main():
    try:
        parse_nrao(nrao_url)
    except ValueError as v:
        print("ValueError: " + str(v))

    with urllib.request.urlopen('https://www.eso.org/public/news') as response:
        data = response.read()
        print(data)

if __name__ == "__main__":
    main()
