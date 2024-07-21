"""
Prac 07 - Project Management
Main Function

"""

import datetime
from project import Project

FILENAME = "projects.txt"
MENU = (
    "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects\n- (A)dd new projects\n- (U)pdate projects\n- ("
    "Q)uit")

def main():
    projects = load_projects(FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    choice = input(MENU).strip().lower()
    while choice != 'q':
        if choice == 'l':
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename to save to: ")
            # save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date = input("Show projects that start after date (dd/mm/yyyy): ")
            # filter_projects_by_date(projects, date)
        elif choice == 'a':
        # add_new_project(projects)
        elif choice == 'u':
        # update_project(projects)
        else:
            print("Invalid choice")

        choice = input(MENU).strip().lower()

    save = input(f"Would you like to save to {FILENAME}? (y/n): ").strip().lower()
    if save == 'y':
    # save_projects(FILENAME, projects)

    print("Thank you for using custom-built project management software.")


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
    """
    Displays incomplete and completed projects sorted by priority.
    """
    incomplete = sorted([project for project in projects if not project.is_complete()])
    complete = sorted([project for project in projects if project.is_complete()])

    print("Incomplete projects: ")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects: ")
    for project in complete:
        print(f"  {project}")


main()
