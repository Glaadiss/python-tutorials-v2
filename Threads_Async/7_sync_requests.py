import requests

urls = [
    "https://imdb.com",
    "https://python.org",
    "https://docs.python.org",
    "https://wikipedia.org",
]


def main():
    for url in urls:
        r = requests.get(url)
        print(url, r.status_code)


if __name__ == "__main__":
    main()
