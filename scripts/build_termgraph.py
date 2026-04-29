#!/usr/bin/env python3

import os
import re


def extract_time_results(input_path: str) -> list[tuple[str, float]]:
    results: list[tuple[str, float]] = []

    pattern = re.compile(r"^([a-zA-Z0-9_]+):\s+([0-9.]+)s$")

    with open(input_path, "r") as file:
        for line in file:
            match = pattern.match(line.strip())

            if match:
                name = match.group(1)
                value = float(match.group(2))
                results.append((name, value))

    return results


def extract_file_reading_result(input_path: str) -> tuple[str, float, float]:
    mode = ""
    memory = 0.0
    time = 0.0

    with open(input_path, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith("Mode:"):
                mode = line.split(":", 1)[1].strip()

            elif line.startswith("Peak Memory Usage"):
                memory = float(line.split("=")[1].replace("GB", "").strip())

            elif line.startswith("User Mode Time + System Mode Time"):
                time = float(line.split("=")[1].replace("s", "").strip())

    return mode, memory, time


def write_single_metric_dat(
    output_path: str,
    title: str,
    rows: list[tuple[str, float]],
) -> None:
    with open(output_path, "w") as file:
        file.write(f"@ {title}\n")

        for name, value in rows:
            file.write(f"{name},{value}\n")


def write_file_reading_dat(
    output_path: str,
    rows: list[tuple[str, float, float]],
) -> None:
    with open(output_path, "w") as file:
        file.write("@ Memory GB, Time Sec\n")

        for mode, memory, time in rows:
            file.write(f"{mode},{memory},{time}\n")


def main() -> None:
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results_dir = os.path.join(project_root, "results")
    data_dir = os.path.join(project_root, "data")

    os.makedirs(data_dir, exist_ok=True)

    benchmark_files = {
        "email_filtering.txt": ("Email Filtering Time", "email_filtering.dat"),
        "sum_squares.txt": ("Sum of Squares Time", "sum_squares.dat"),
        "counter_benchmark.txt": ("Counter Benchmark Time", "counter_benchmark.dat"),
    }

    for input_name, (title, output_name) in benchmark_files.items():
        input_path = os.path.join(results_dir, input_name)
        output_path = os.path.join(data_dir, output_name)

        rows = extract_time_results(input_path)
        write_single_metric_dat(output_path, title, rows)

        print(f"Created: {output_path}")

    file_reading_rows = [
        extract_file_reading_result(
            os.path.join(results_dir, "file_reading_ordinary.txt")
        ),
        extract_file_reading_result(
            os.path.join(results_dir, "file_reading_generator.txt")
        ),
    ]

    file_reading_path = os.path.join(data_dir, "file_reading.dat")
    write_file_reading_dat(file_reading_path, file_reading_rows)

    print(f"Created: {file_reading_path}")


if __name__ == "__main__":
    main()
