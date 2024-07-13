"""Emails
Estimate time:20 minutes
Actual:35 minutes

"""


def main():
    """Program that converts emails to names and stores them  a dictionary"""
    emails_to_names = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        name_check = input(f"Is {name} your name? Y/N  ").upper()
        if name_check != "Y":
            name = input("Enter your name: ")
        emails_to_names[email] = name
        email = input("Email: ")
    for email, name in emails_to_names.items():
        print(f"{name} ({email})")


def get_name(email):
    """Returns the name extracted from the email"""
    title = email.split("@")[0]
    parts = title.split(".")
    name = " ".join(parts).title()
    return name


main()
