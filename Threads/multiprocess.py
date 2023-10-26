import multiprocessing
import os
import time

import psutil


def long_loop(num_iterations):
    for _ in range(num_iterations):
        pass


def run_without_multiprocessing(loop_length, num_processes):
    start_time = time.time()
    for _ in range(num_processes):
        long_loop(loop_length)
    end_time = time.time()
    return end_time - start_time


def run_with_multiprocessing(loop_length, num_processes):
    processes = []
    start_time = time.time()

    for _ in range(num_processes):
        p = multiprocessing.Process(target=long_loop, args=(loop_length,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()
    return end_time - start_time


if __name__ == "__main__":
    # Get the number of physical cores
    NUM_PROCESSES = psutil.cpu_count(logical=False)

    LOOP_LENGTH = 10**7

    time_without_mp = run_without_multiprocessing(LOOP_LENGTH, NUM_PROCESSES)
    print("Time without multiprocessing:", time_without_mp)

    time_with_mp = run_with_multiprocessing(LOOP_LENGTH, NUM_PROCESSES)
    print("Time with multiprocessing:", time_with_mp)
