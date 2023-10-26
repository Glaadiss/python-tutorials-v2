import asyncio
import concurrent.futures
import time

import aiohttp

urls = [
    "https://imdb.com",
    "https://python.org",
    "https://docs.python.org",
    "https://wikipedia.org",
]


async def get_from(session, url):
    async with session.get(url) as r:
        print(r.status)
        return await r.text()


def cpu_bound_task(delay):
    print("process task started")
    # simulate a CPU-bound task
    time.sleep(delay)
    return f"CPU-bound task completed after {delay} seconds"


async def run_in_executor(delay):
    loop = asyncio.get_running_loop()
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_bound_task, delay)
        print(result)
        return result


async def run_requests():
    async with aiohttp.ClientSession() as session:  # What is it for?
        datas = await asyncio.gather(*[get_from(session, u) for u in urls])
        return [_[:200] for _ in datas]


async def main():
    data = await asyncio.gather(run_in_executor(0.1), run_in_executor(1), run_in_executor(2), run_requests())
    print(data)


if __name__ == "__main__":
    asyncio.run(main())
