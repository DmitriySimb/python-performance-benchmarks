#!/usr/bin/env python3

import timeit
from functools import reduce


def loop_sum_squares(number: int) -> int:
    result = 0

    for value in range(1, number + 1):
        result += value * value

    return result


def reduce_sum_squares(number: int) -> int:
    return reduce(
        lambda current_sum, value: current_sum + value * value,
        range(1, number + 1),
        0,
    )


def run_sum_squares_benchmark(calls: int, number: int) -> list[tuple[str, float]]:
    benchmarks = {
        "loop": lambda: loop_sum_squares(number),
        "reduce": lambda: reduce_sum_squares(number),
    }

    results: list[tuple[str, float]] = []

    for name, function in benchmarks.items():
        elapsed_time = timeit.timeit(function, number=calls)
        results.append((name, elapsed_time))

    return sorted(results, key=lambda item: item[1])


def print_sum_squares_benchmark(calls: int, number: int) -> None:
    results = run_sum_squares_benchmark(calls, number)

    print("Sum of squares benchmark")
    print(f"Calls: {calls}")
    print(f"Number: {number}")
    print()

    for name, elapsed_time in results:
        print(f"{name}: {elapsed_time:.9f}s")

    print()
    print(f"Best method: {results[0][0]}")
