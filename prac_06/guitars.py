""""
Prac 06
Main Guitars Function
Time Taken 20 minutes
"""
from guitar import Guitar


def main():
    """Guitar Program that functions by Guitar Class"""
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
    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars):
            vintage_guitar = ""
            if guitar.is_vintage():
                vintage_guitar = " (vintage)"
            print(f"Guitar {i + 1:20}:  {guitar.name:10} ({guitar.year}, is worth ${guitar.cost:.2f}"
                  f"{vintage_guitar}")


main()
