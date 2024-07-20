"""
Prac 06 - guitar

class Guitar

"""
CURRENT_YEAR = 2024
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Guitar constructor fields"""
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def get_age(self):
        """Gets current age of guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determines if guitar is vintage based on current age"""
        return self.get_age() >= VINTAGE_AGE

    def __str__(self):
        """Returns string representation of Guitar"""
        return f"{self.name} ({self.year}) ${self.cost}"
