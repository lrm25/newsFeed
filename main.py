import urllib.request

from bs4 import BeautifulSoup

def main():
    print("news feed")
    with urllib.request.urlopen('http://public.nrao.edu/news') as response:
        data = response.read()
        data_soup = BeautifulSoup(data, 'html.parser')
        news_section = data_soup.find_all("div", class_="all-news")
        print(news_section)

if __name__ == "__main__":
    main()
