"""
Prac 09 - Taxi Simulator
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU_OPTIONS = "q(uit, c(hose Taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_cost = 0
    print("Welcome to the Taxi Simulator" + '\n' + MENU_OPTIONS)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxi's Available: ")
            display_available_taxis(taxis)
            taxi_choice = int(input("Choose your taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid choice")
        elif choice == "d":
            if current_taxi == True:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_cost += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_cost:.2f}")
        print(MENU_OPTIONS)
        choice = input(">>> ").lower()


def display_available_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i+1} - {taxi}")


main()
