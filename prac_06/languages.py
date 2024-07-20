from programming_languages import ProgrammingLanguages


def main():
    """This is the main function of the program."""
    python = ProgrammingLanguages("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguages("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguages("Visual Basic", "Static", False, 1991)
    print(f"{python}\n{ruby}\n{visual_basic}")
    languages = [python, ruby, visual_basic]
    print("The Dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
