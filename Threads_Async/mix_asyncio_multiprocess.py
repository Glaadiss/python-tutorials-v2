import asyncio
import concurrent.futures
import time


def cpu_bound_task(delay):
    # simulate a CPU-bound task
    time.sleep(delay)
    return "CPU-bound task completed"


async def run_in_executor():
    loop = asyncio.get_running_loop()
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_bound_task)
        print(result)


async def main():
    await run_in_executor()


if __name__ == "__main__":
    asyncio.run(main())
