#!/usr/bin/env python3

import os
from datetime import datetime


def get_results_dir() -> str:
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results_dir = os.path.join(project_root, "results")

    os.makedirs(results_dir, exist_ok=True)

    return results_dir


def save_text_result(filename: str, content: str) -> str:
    results_dir = get_results_dir()
    output_path = os.path.join(results_dir, filename)

    with open(output_path, "w") as file:
        file.write(content)

    return output_path


def format_header(title: str) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"{title}\nGenerated at: {timestamp}\n{'-' * 40}\n\n"
