#!/usr/bin/env python3

import resource


def read_all_lines(path: str) -> list[str]:
    with open(path, "r") as file:
        return file.readlines()


def read_lines_generator(path: str):
    with open(path, "r") as file:
        for line in file:
            yield line


def get_resource_usage() -> tuple[float, float]:
    usage = resource.getrusage(resource.RUSAGE_SELF)

    peak_memory_gb = usage.ru_maxrss / (1024**3)
    total_time = usage.ru_utime + usage.ru_stime

    return peak_memory_gb, total_time


def run_ordinary_reader(path: str) -> tuple[float, float]:
    lines = read_all_lines(path)

    for _ in lines:
        pass

    return get_resource_usage()


def run_generator_reader(path: str) -> tuple[float, float]:
    for _ in read_lines_generator(path):
        pass

    return get_resource_usage()


def run_file_reading_benchmark(path: str, mode: str) -> tuple[float, float]:
    if mode == "ordinary":
        return run_ordinary_reader(path)

    if mode == "generator":
        return run_generator_reader(path)

    raise ValueError("Mode must be either 'ordinary' or 'generator'")
