import csv, sqlite3, random

def intput(prompt: str = "") -> int:
    try:
        return int(input(prompt))
    except ValueError:
        return intput(prompt)

def floatput(prompt: str = "") -> float:
    try:
        return float(input(prompt))
    except ValueError:
        return floatput(prompt)

with open("moo.csv", "r") as file:
    print(list(csv.reader(file)))

with open("moo.csv", "r") as file:
    print(list(csv.DictReader(file)))

with open("Bank.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    for _ in range(0, 100):
        csv_writer.writerow([random.randint(10, 99) for _ in range(5)])

with open("Bank.csv", "r") as file:
    for row in csv.reader(file):
        print(row)

with open("Bonk.csv", "w", newline="") as file:
    csv_writer = csv.DictWriter(file, [chr(38 + i) for i in range(5)])
    csv_writer.writeheader()
    for _ in range(0, 100):
        csv_writer.writerow({chr(38 + i): chr(random.randint(32, 126)).replace("\\", "/") for i in range(5)})

with open("Bonk.csv", "r") as file:
    for row in csv.DictReader(file):
        print(row)