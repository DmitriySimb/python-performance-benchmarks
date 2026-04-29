#!/usr/bin/env python3

import random
import timeit
from collections import Counter


def generate_data(
    size: int = 1_000_000, min_value: int = 0, max_value: int = 100
) -> list[int]:
    random.seed(42)
    return [random.randint(min_value, max_value) for _ in range(size)]


def count_with_dict(data: list[int]) -> dict[int, int]:
    result = {number: 0 for number in range(101)}

    for number in data:
        result[number] += 1

    return result


def top10_with_dict(data: list[int]) -> dict[int, int]:
    counts: dict[int, int] = {}

    for number in data:
        counts[number] = counts.get(number, 0) + 1

    sorted_items = sorted(
        counts.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    return dict(sorted_items[:10])


def count_with_counter(data: list[int]) -> dict[int, int]:
    return dict(Counter(data))


def top10_with_counter(data: list[int]) -> dict[int, int]:
    return dict(Counter(data).most_common(10))


def run_counter_benchmark(size: int = 1_000_000) -> list[tuple[str, float]]:
    data = generate_data(size)

    benchmarks = {
        "manual_count": lambda: count_with_dict(data),
        "counter_count": lambda: count_with_counter(data),
        "manual_top10": lambda: top10_with_dict(data),
        "counter_top10": lambda: top10_with_counter(data),
    }

    results: list[tuple[str, float]] = []

    for name, function in benchmarks.items():
        elapsed_time = timeit.timeit(function, number=1)
        results.append((name, elapsed_time))

    return sorted(results, key=lambda item: item[1])


def print_counter_benchmark(size: int = 1_000_000) -> None:
    results = run_counter_benchmark(size)

    print("Counter benchmark")
    print(f"Data size: {size}")
    print()

    for name, elapsed_time in results:
        print(f"{name}: {elapsed_time:.7f}s")
