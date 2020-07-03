import urllib.request

from bs4 import BeautifulSoup

def main():
    print("news feed")
    with urllib.request.urlopen('http://public.nrao.edu/news') as response:
        data = response.read()
        data_soup = BeautifulSoup(data, 'html.parser')
        news_titles = data_soup.find_all("div", class_="news-list-title")
        for news_title in news_titles:
            print(news_title.text)

if __name__ == "__main__":
    main()
