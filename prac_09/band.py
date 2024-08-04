"""
Prac 09 - Band Class

"""
class Band:
    def __init__(self, name):
        """Initialize Band object"""
        self.name = name
        self.members = []

    def __str__(self):
        """String representation of Band object"""
        members = ', '.join(f"{member.name} ({member})" for member in self.members)
        return f"{self.name} ({members})"

    def play(self):
        """Play the band"""
        output = []
        for member in self.members:
            output.append(member.play())
        return "\n".join(output)

    def add(self, musician):
        """Add a musician to the band"""
        self.members.append(musician)
