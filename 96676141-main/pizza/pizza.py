import sys
import csv
import os
from tabulate import tabulate

details = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    file_path = sys.argv[1]

    if not file_path.lower().endswith(".csv"):
        sys.exit("Not a CSV file")

    if not os.path.exists(file_path):
        sys.exit("File does not exist")

    with open(sys.argv[1], "r") as file:
        for line in file:
            details.append(line.strip().split(","))

table = tabulate(details, headers="firstrow", tablefmt="grid")

print(table)

