"""
Prac 09 - Unreliable Car

"""

from car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        reliability_chance = randint(1, 100)
        if reliability_chance > self.reliability + 1:
            distance = 0
        distance_drove = super().drive(distance)
        return distance_drove
