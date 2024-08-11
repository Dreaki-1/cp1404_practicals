from prac_09.silver_service_taxi import SilverServiceTaxi


def run_test():
    taxi = SilverServiceTaxi("Lexus RC", 100, 5)
    taxi.drive(10)
    print(taxi)
    print(taxi.get_fare())



run_test()