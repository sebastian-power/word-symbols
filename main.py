import csv

with open("symbols.csv", "r", encoding="UTF-8", newline="") as symbols_data:
    reader = csv.reader(symbols_data)
    for line in reader:
        print(line)
