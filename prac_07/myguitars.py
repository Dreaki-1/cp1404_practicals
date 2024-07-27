"""
Prac 07

Guitars

"""
import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    load_csv(FILENAME)
    guitars = []
    print("My guitars!")
    name = input("Name:")
    while name != "":
        year = int(input("Year:"))
        cost = float(input("Cost:"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar.name} ({new_guitar.year}) : ${new_guitar.cost:.2f}  added.")
        name = input("Name:")
    else:
        sorted_guitars = sorted(guitars)
        append_guitar(sorted_guitars, FILENAME)


def load_csv(file):
    guitars = []
    with open(file, "r", newline="") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            guitars.append(row)
    return guitars


def append_guitar(guitars, file):
    with open(file, "a", newline="") as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow(guitar.csv_convert())


main()
