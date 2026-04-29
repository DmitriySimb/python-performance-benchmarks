#!/bin/bash

echo "=== Email filtering ==="
python3 main.py email 1000000

echo
echo "=== Sum of squares ==="
python3 main.py squares 1000000 5

echo
echo "=== Counter ==="
python3 main.py counter

echo
echo "=== File reading ==="
python3 main.py file ordinary data/ratings.csv
python3 main.py file generator data/ratings.csv

echo
echo "=== Build termgraph data ==="
python3 scripts/build_termgraph.py
