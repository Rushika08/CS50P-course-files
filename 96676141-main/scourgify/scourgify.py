import sys
import os
import csv

details = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    file_path = sys.argv[1]

    if not file_path.lower().endswith(".csv"):
        sys.exit(f"Could not read {file_path}")

    if not os.path.exists(file_path):
        sys.exit(f"Could not read {file_path}")

    with open(sys.argv[1], "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            name_parts = row[0].split(", ")
            last_name = name_parts[0]
            first_name = name_parts[1]

            house = row[1]

            details.append((first_name, last_name, house))

with open(sys.argv[2], "w", newline='') as file2:
    csv_writer = csv.writer(file2)
    csv_writer.writerow(["first","last","house"])
    for line in details:
        csv_writer.writerow(line)


