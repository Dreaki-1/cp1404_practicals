from prac_09.unreliable_car import UnreliableCar


def run_test():
    """Reliable"""
    car = UnreliableCar("Toyota", 100, 99)
    for i in range(1, 15):
        print(f"{car.name} drove {car.drive(i)} km")
    print(f"{car}\n")
    """Unreliable"""
    car2 = UnreliableCar("Fiat", 100, 5)
    for i in range(1, 15):
        print(f"{car2.name} drove {car2.drive(i)} km")
    print(car2)


run_test()
