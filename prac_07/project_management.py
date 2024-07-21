"""
Prac 07 - Project Management
Main Function

"""
import csv
import datetime
from project import Project

FILENAME = "projects.txt"
MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects\n- (A)dd new projects\n- (U)pdate projects\n- ("
        "Q)uit")


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(MENU)
    print(f"Loaded {len(projects) - 1} projects from {FILENAME}")
    choice = input(">>> ").upper()
    while choice != "Q"
        if choice == "L":
            load_projects(projects)
        elif choice == "S":
            pass
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        elif choice == "Q":
            pass
        print("invalid choice")
        print(MENU)
        choice = input(">>> ").upper()




def load_projects(filename):
    """
    Loads projects from a file.
    """
    projects = []
    with open(filename, 'r') as file:
        lines = file.readlines()[1:]  # Skip header
        for line in lines:
            parts = line.strip().split('\t')
            projects.append(Project(*parts))
    return projects


def display_projects(projects):
    complete_projects = [project for project in projects.completion_percentage if projects.completion_percentage == 100]
    incomplete_projects = [project for project in projects.completion_percentage if project.completion_percentage < 100]
    print("Completed projects:")
    for project in complete_projects:
        print(project)
    print("\nIncomplete projects:")
    for project in incomplete_projects:
        print(project)

main()
