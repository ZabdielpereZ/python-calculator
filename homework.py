# Calculator app

from helper import d, fd, welcome, clear, reset, exit 
from operations import addition, subtraction, division, multiply, exponents 


def main():
    welcome()
    while True:
        action = input(''' select an action you'd like to preform:

1 - Addition
2 - Subtraction
3 - Division
4 - Multiplication
5 - Exponents
6 - Quit
''')
        
        if action == '1':
            reset()
            addition()
        elif action == '2':
            reset()
            subtraction()
        elif action == '3':
            reset()
            division()
        elif action == '4':
            reset()
            multiply()
        elif action == '5':
            reset()
            exponents()
        elif action == '6':
            exit()
            break


main()