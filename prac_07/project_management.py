"""
Prac 07 - Project Management
Main Function
Estimated Time: 4.5 hours
"""

import datetime
from project import Project

FILENAME = "projects.txt"
MENU = (
    "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects\n- (A)dd new projects\n- (""U)pdate projects\n- ("
    "Q)uit")


def main():
    projects = load_projects(FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    choice = input(MENU + "\n>>>").strip().lower()
    while choice != 'q':
        if choice == 'l':
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid choice")

        choice = input(MENU + "\n>>>").strip().lower()

    save = input(f"Would you like to save to {FILENAME}? (y/n): ").strip().lower()
    if save == 'y':
        save_projects(FILENAME, projects)

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


def save_projects(filename, projects):
    """
    Saves projects to a file.
    """
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")


def filter_projects_by_date(projects, date):
    """
    Filters and displays projects that start after a given date, sorted by start date.
     Date to filter projects by in 'dd/mm/yyyy' format
    """
    filtered = sorted([p for p in projects if p.starts_after(date)], key=Project.get_start_date)
    for project in filtered:
        print(project)


def update_project(projects):
    """
    Updates an existing project in the list of projects.
    """
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    choice = int(input("Project choice: "))
    project = projects[choice]

    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")

    project.update(new_percentage or None, new_priority or None)


def add_new_project(projects):
    """
    Adds a new project to the list of projects.
    """
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion_percentage = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


main()
