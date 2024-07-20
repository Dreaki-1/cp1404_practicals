"""
Prac 06
PROGRAMMING LANGUAGES
Time taken to complete : 15 minutes

"""


class ProgrammingLanguages:
    """Divide programming languages into parts by their nane, typing method, reflection and year of creation"""

    def __init__(self, name="", typing="", reflection="", year=0):
        """Applies a variable to each part of ProgramingLanguage class"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check whether language uses dynamic typing"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Returns a string representation of the ProgrammingLanguages class"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
