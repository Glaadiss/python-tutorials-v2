import asyncio
import time

import psutil


def long_loop_seq(num_iterations):
    for _ in range(num_iterations):
        pass


async def long_loop(num_iterations):
    for _ in range(num_iterations):
        pass


async def main(loop_length, num_tasks):
    tasks = [long_loop(loop_length) for _ in range(num_tasks)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    LOOP_LENGTH = 10**7
    NUM_TASKS = psutil.cpu_count(logical=False)

    start_time = time.time()
    long_loop_seq(LOOP_LENGTH * NUM_TASKS)
    end_time = time.time()

    print("Time without asyncio:", end_time - start_time)

    start_time = time.time()
    asyncio.run(main(LOOP_LENGTH, NUM_TASKS))
    end_time = time.time()

    print("Time with asyncio:", end_time - start_time)
