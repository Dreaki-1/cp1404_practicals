"""
Prac 09 - Taxi test

"""

from taxi import Taxi


def run_test():
    my_taxi = Taxi("Prius 1", 100, 1.23)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)





run_test()
