"""
Prac 07 - Project Management
Main Function

"""
import csv
import datetime

FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave Projects\n"

def main():
    print("Welcome to Pythonic Project Management")
    data = load_projects(FILENAME)
    print(f"Loaded {len(data)-1} projects from {FILENAME}")
    choice = input(">>> ").lower()
    while choice != True:
        if choice == "L":
            load_projects(data)
        elif choice == "S":
            pass
        elif choice == "D":
            display_projects()
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        elif choice == "Q":
            pass
        print("invalid choice")
        choice = input(">>> ").lower()

# quit_program()


def load_projects(file):
    projects = []
    with open(file) as infile:
        reader = csv.reader(infile)
        for row in reader:
            projects.append(row)
    return projects

def display_projects():
    projects = []
    projects_completed = []
    for project in projects if project[4] = 100:
        projects.append(project)




main()