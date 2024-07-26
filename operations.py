def addition():
    '''Get inputs and b from the user and add them together.'''
    while True:
        try:
            a = int(input("Please enter the frist number for the addition operation: "))
            b = int(input("Please enter the second number: "))
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"Oops, unexpected error: {e}")
        else:
            print(f"The result of adding {a} + {b} = {a + b}")
            break

def subtraction():
    '''Get inputs a and b from the user and subtract.'''
    while True:
        try:
            a = float(input("Please enter the frist number for the subtraction operation: "))
            b = float(input("Please enter the second number: "))
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"Oops, unexpected error: {e}")
        else:
            print(f"The result of subtracting {b} - {a} = {a - b}")
            break

def division():
    '''Get inputs a and b from the user and divide.'''
    while True:
        try:
            a = float(input("Please enter the frist number for the division operation: "))
            b = float(input("Please enter the second number: "))
            ans = a/b
        except ValueError:
            print("Please enter valid numbers!")
        except ZeroDivisionError:
            print("Cannot divide by zero!")
        except Exception as e:
            print(f"Oops, unexpected error: {e}")
        else:
            print(f"The result of dividing {a} / {b} = {round(ans, 2)}")
            break

def multiply():
    '''Get inputs a and b from the user and multiply.'''
    while True:
        try:
            a = float(input("Please enter the frist number for the multiplication operation: "))
            b = float(input("Please enter the second number: "))
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"Oops, unexpected error: {e}")
        else:
            print(f"The result of multiplying {a} x {b} = {a * b}")
            break

def exponents():
    '''Get inputs a and b from the user and raises a to the powerof b.'''
    while True:
        try:
            a = int(input("Please enter the base number: "))
            b = int(input("Please enter the exponent: "))
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"Oops, unexpected error: {e}")
        else:
            print(f"The result of {a} raised to the power of {b} = {a ** b}")
            break