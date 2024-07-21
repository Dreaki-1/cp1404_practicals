"""Project Management System

Estimated Time: 5 hours
"""

from datetime import datetime


class Project:
    """Represents a project with attributes such as name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """
        Initializes a Project object.
        """
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __repr__(self):
        """
        Returns a string representation of the Project object.
        """
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """
        Less than comparison for sorting projects by priority.
        """
        return self.priority < other.priority

    def __eq__(self, other):
        """
        Equality comparison for projects.
        """
        return self.priority == other.priority

    def is_complete(self):
        """
        Checks if the project is complete.

        """
        return self.completion_percentage == 100

    def update(self, completion_percentage=None, priority=None):
        """
        Updates the completion percentage and/or priority of the project.
        """
        if completion_percentage is not None:
            self.completion_percentage = int(completion_percentage)
        if priority is not None:
            self.priority = int(priority)

    def starts_after(self, date):
        """
        Checks if the project starts after a given date.
        """
        return self.start_date > datetime.strptime(date, "%d/%m/%Y")

    def get_priority(self):
        """
        Gets the priority of the project.
        """
        return self.priority

    def get_start_date(self):
        """
        Gets the start date of the project.
        """
        return self.start_date