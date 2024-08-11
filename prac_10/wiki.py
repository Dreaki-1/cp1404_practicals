"""
Prac 10 - Wiki

"""


import wikipedia
# Test
barack = wikipedia.search("Barack")
print(barack)

# SIMPLE
choice = input("What would you like to search on wiki >>>")
while choice != "":
    print(wikipedia.summary(choice))
    choice = input("What would you like to search on wiki >>>")
print("Thank you for using Wiki")


# With Error handling
title = input("Enter page title: ")
while title != "":
    try:
        print(wikipedia.page(title, auto_suggest=False))
        print(wikipedia.summary(title))
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"We need a more specific title. Try one of the following, or a new search:\n {e.options}")
    except wikipedia.exceptions.PageError:
        print(f"Page id {title} does not match any pages. Try another id!")
    title = input("Enter page title: ")
print("Thank you for using Wiki")



