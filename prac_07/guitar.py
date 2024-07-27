"""
Prac 06 now prac 07 - guitar

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

    def __lt__(self, other):
        return self.year < other.year

    def csv_convert(self):
        return [self.name, self.year, self.cost]

    def __repr__(self):
        """Returns string representation of Guitar"""
        return f"{self.name} ({self.year}) ${self.cost}"



# def run_test():
#     """Runs tests"""
#
#     guitar1 = Guitar("gibson", 2000, 5000)
#     guitar2 = Guitar("Alexandra 92", 1800, 11050)
#     guitar3 = Guitar("Brazil", 1900, 2000)
#
#     guitars= [guitar1, guitar2, guitar3]
#     sorted_guitars = sorted(guitars)
#
#     print(sorted_guitars)
#
#
# run_test()
