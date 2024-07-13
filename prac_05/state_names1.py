"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
"""LBYL"""

state = input("Enter short state: ").upper()
while state != "":
    if state in CODE_TO_NAME:
        print(state, "is", CODE_TO_NAME[state])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

"""EAFP"""
while True:
    try:
        state = input("Enter short state: ").upper()
        print(f"{state} is {CODE_TO_NAME[state]}")
    except KeyError:
        print("Invalid state")
    else:
        print("Goodbye")
        break

"""For part 4."""
for state_abbreviation, state_name in CODE_TO_NAME.items():
    print(f"{state_abbreviation:3} is {state_name}")
