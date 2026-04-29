#!/usr/bin/env python3

import sys

from benchmarks.counter_benchmark import run_counter_benchmark
from benchmarks.email_filtering import run_email_filtering_benchmark
from benchmarks.file_reading import run_file_reading_benchmark
from benchmarks.sum_squares import run_sum_squares_benchmark
from utils.save_results import format_header, save_text_result


def print_usage() -> None:
    print("Usage:")
    print("  python3 main.py email <calls>")
    print("  python3 main.py squares <calls> <number>")
    print("  python3 main.py counter [size]")
    print("  python3 main.py file <ordinary|generator> <path>")


def save_and_print(filename: str, content: str) -> None:
    print(content)

    output_path = save_text_result(filename, content)
    print(f"\nResult saved to: {output_path}")


def run_email(args: list[str]) -> None:
    if len(args) != 1:
        print_usage()
        return

    calls = int(args[0])
    results = run_email_filtering_benchmark(calls)

    content = format_header("Email Filtering Benchmark")
    content += f"Calls: {calls}\n\n"

    for name, elapsed_time in results:
        content += f"{name}: {elapsed_time:.9f}s\n"

    content += f"\nBest method: {results[0][0]}\n"

    save_and_print("email_filtering.txt", content)


def run_squares(args: list[str]) -> None:
    if len(args) != 2:
        print_usage()
        return

    calls = int(args[0])
    number = int(args[1])
    results = run_sum_squares_benchmark(calls, number)

    content = format_header("Sum of Squares Benchmark")
    content += f"Calls: {calls}\n"
    content += f"Number: {number}\n\n"

    for name, elapsed_time in results:
        content += f"{name}: {elapsed_time:.9f}s\n"

    content += f"\nBest method: {results[0][0]}\n"

    save_and_print("sum_squares.txt", content)


def run_counter(args: list[str]) -> None:
    if len(args) > 1:
        print_usage()
        return

    size = int(args[0]) if args else 1_000_000
    results = run_counter_benchmark(size)

    content = format_header("Counter Benchmark")
    content += f"Data size: {size}\n\n"

    for name, elapsed_time in results:
        content += f"{name}: {elapsed_time:.7f}s\n"

    save_and_print("counter_benchmark.txt", content)


def run_file(args: list[str]) -> None:
    if len(args) != 2:
        print_usage()
        return

    mode = args[0]
    path = args[1]

    peak_memory_gb, total_time = run_file_reading_benchmark(path, mode)

    content = format_header("File Reading Benchmark")
    content += f"Mode: {mode}\n"
    content += f"File: {path}\n\n"
    content += f"Peak Memory Usage = {peak_memory_gb:.3f} GB\n"
    content += f"User Mode Time + System Mode Time = {total_time:.2f}s\n"

    save_and_print(f"file_reading_{mode}.txt", content)


def main() -> None:
    if len(sys.argv) < 2:
        print_usage()
        return

    benchmark_name = sys.argv[1]
    args = sys.argv[2:]

    if benchmark_name == "email":
        run_email(args)
    elif benchmark_name == "squares":
        run_squares(args)
    elif benchmark_name == "counter":
        run_counter(args)
    elif benchmark_name == "file":
        run_file(args)
    else:
        print_usage()


if __name__ == "__main__":
    main()
