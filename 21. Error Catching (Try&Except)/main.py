try:
    number = int(input("Enter a number: "))
    print(number)
except:  # this will catch any error that may occur
    print("No integer was entered")

try:
    num = 10 / 0  # will throw ZeroDivisionError
    # number = int(input("Enter a number: ")) # can throw ValueError (determained by user input)
except ZeroDivisionError:  # will specifically catch zero division errors
    print("You cannot divide by 0")
    # raise ValueError("Another error, but this one was raised") # raise an error
# will catch errors where you try to convert text(a, b, c...) to integer
except ValueError:
    print("Invalid input!")

try:
    # num2 = "2" + 4
    num = 10 / 0
except ZeroDivisionError as err:  # store error in a variable
    print(err)  # prints out what went wrong
except (ValueError, TypeError):  # allows you to catch multiple errors
    print("Value or Type error occured!")

try:
    num = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print("This code will run, wether there is an exception or not")

try:
    x = 10
except Exception as e:
    print("error occured: " + e)
else:  # if no error occured
    print("No errors were found")


# DO NOT CREATE TUTORIAL OF BELOW!!!!!
# create your own error (has to extend Exception)


class ValueTooHighError(Exception):
    # NOTE: you do not have to create a custom init function!
    # You can just say pass if you want to.
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test(x):
    if x > 100:
        raise ValueTooHighError("Value is too high:", x)


try:
    test(200)
except ValueTooHighError as err:
    print(err.message, err.value)


x = -1
if x < 0:
    raise Exception("x should be positive")  # throw an error

assert(x >= 0), "x is smaller than 0"  # throws error if condition is not true
