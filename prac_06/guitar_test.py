"""
Prac 06
Guitar Test


"""

from guitar import Guitar


def run_test():
    """Runs test for Guitar class"""
    guitar1 = Guitar("Guitar TEST1", 2000, 1234.45)
    guitar2 = Guitar("Guitar TEST2", 1900, 15000)
    guitar3 = Guitar("Guitar TEST3", 1974, 9999)
    print(f"{guitar1.name} Should be {24} and is {guitar1.get_age()}")
    print(f"{guitar1.name} Should be {False} and is {guitar1.is_vintage()}")
    print(f"{guitar2.name} Should be {124} and is {guitar2.get_age()}")
    print(f"{guitar2.name} Should be {True} and is {guitar2.is_vintage()}")
    print(f"{guitar3.name} Should be {50} and is {guitar3.get_age()}")
    print(f"{guitar3.name} Should be {True} and is {guitar3.is_vintage()}")


run_test()
