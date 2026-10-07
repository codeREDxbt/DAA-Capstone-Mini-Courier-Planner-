"""
Project: Mini Courier Planner
Author: Vinayak Vashisth (Roll No: 2501730150)
Programme: B.Tech CSE (AI & ML)
Course: Design and Analysis of Algorithms (DAA)
"""

# Performance measurement utilities

import time


def measure_time(function, *args):
    """
    Measure the execution time of a function.

    Returns:
        result: Function output
        runtime: Execution time in seconds
    """

    start_time = time.perf_counter()

    result = function(*args)

    end_time = time.perf_counter()

    runtime = end_time - start_time

    return result, runtime