"""
Prac 09 - Silver Service Taxi

"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4

    def __init__(self, name, fuel, fanciness):
        """Initialize the SilverServiceTaxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def retrieve_fare(self):
        """Retrieves the fare of the ride"""
        return self.flagfall + super().get_fare()

    def __str__(self):
        """String representation of SilverServiceTaxi"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"