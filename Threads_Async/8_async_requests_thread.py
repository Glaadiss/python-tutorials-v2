import asyncio

import requests

urls = [
    "https://imdb.com",
    "https://python.org",
    "https://docs.python.org",
    "https://wikipedia.org",
]


def request(url):
    r = requests.get(url)
    print(url, r.status_code)


async def main():
    reqs = []
    for url in urls:
        reqs.append(asyncio.to_thread(request, url))

    res = await asyncio.gather(*reqs)
    print(res)


if __name__ == "__main__":
    asyncio.run(main())
