import os


def clear_screen():

    if os.name == "nt":
        os.system('cls')

    elif os.name == "posix":
        os.system('clear')


