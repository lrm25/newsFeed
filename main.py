import urllib.request

def main():
    print("news feed")
    with urllib.request.urlopen('http://public.nrao.edu/news') as response:
        data = response.read()
        print(data)

if __name__ == "__main__":
    main()
