#!/usr/bin/env python3

import timeit


EMAILS = [
    "john@gmail.com",
    "james@gmail.com",
    "alice@yahoo.com",
    "anna@live.com",
    "philipp@gmail.com",
] * 5


def loop_search(emails: list[str]) -> list[str]:
    result: list[str] = []

    for email in emails:
        if email.endswith("@gmail.com"):
            result.append(email)

    return result


def list_comprehension_search(emails: list[str]) -> list[str]:
    return [email for email in emails if email.endswith("@gmail.com")]


def map_search(emails: list[str]) -> list[str]:
    mapped = map(
        lambda email: email if email.endswith("@gmail.com") else None,
        emails,
    )

    return [email for email in mapped if email is not None]


def filter_search(emails: list[str]) -> list[str]:
    return list(filter(lambda email: email.endswith("@gmail.com"), emails))


def run_email_filtering_benchmark(number: int) -> list[tuple[str, float]]:
    benchmarks = {
        "loop": lambda: loop_search(EMAILS),
        "list_comprehension": lambda: list_comprehension_search(EMAILS),
        "map": lambda: map_search(EMAILS),
        "filter": lambda: filter_search(EMAILS),
    }

    results: list[tuple[str, float]] = []

    for name, function in benchmarks.items():
        elapsed_time = timeit.timeit(function, number=number)
        results.append((name, elapsed_time))

    return sorted(results, key=lambda item: item[1])


def print_email_filtering_benchmark(number: int) -> None:
    results = run_email_filtering_benchmark(number)

    print("Email filtering benchmark")
    print(f"Calls: {number}")
    print()

    for name, elapsed_time in results:
        print(f"{name}: {elapsed_time:.9f}s")

    print()
    print(f"Best method: {results[0][0]}")
