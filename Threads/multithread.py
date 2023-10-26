import os
import threading
import time

import psutil


def long_loop(num_iterations):
    for _ in range(num_iterations):
        pass


def run_without_multithreading(loop_length, num_threads):
    start_time = time.time()
    for _ in range(num_threads):
        long_loop(loop_length)
    end_time = time.time()
    return end_time - start_time


def run_with_multithreading(loop_length, num_threads):
    threads = []
    start_time = time.time()

    for _ in range(num_threads):
        t = threading.Thread(target=long_loop, args=(loop_length,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()
    return end_time - start_time


if __name__ == "__main__":
    # Get the number of physical cores
    NUM_THREADS = psutil.cpu_count(logical=False)

    LOOP_LENGTH = 10**7

    time_without_mt = run_without_multithreading(LOOP_LENGTH, NUM_THREADS)
    print("Time without multithreading:", time_without_mt)

    time_with_mt = run_with_multithreading(LOOP_LENGTH, NUM_THREADS)
    print("Time with multithreading:", time_with_mt)
