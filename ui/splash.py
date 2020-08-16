from pyfiglet import Figlet
from os import system, name
from clint.textui import colored

f = Figlet(font='slant')


def splash():
    print(colored.blue(f.renderText('Sanbercode')))


def close():
    print(colored.red(f.renderText('Thank You')))
    print("Created by Riyad Febrian")


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
