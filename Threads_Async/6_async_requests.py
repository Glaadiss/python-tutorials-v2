import asyncio

import aiohttp

urls = [
    "https://imdb.com",
    "https://python.org",
    "https://docs.python.org",
    "https://wikipedia.org",
]


async def get_from(session, url):
    async with session.get(url) as r:  # What is it for?
        return await r.text()


async def main():
    async with aiohttp.ClientSession() as session:  # What is it for?
        datas = await asyncio.gather(*[get_from(session, u) for u in urls])
        print([_[:200] for _ in datas])


if __name__ == "__main__":
    asyncio.run(main())
