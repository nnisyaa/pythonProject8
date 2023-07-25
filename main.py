# Task 1
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


num = is_even(10)
print(num)

# Task 2


def is_odd(number1):
    if number1 % 2 == 1:
        return True
    else:
        return False


num1 = is_odd(11)
print(num1)
# Task3


def is_negative(number2):
    if number2 < 0:
        return True
    else:
        return False


num2 = is_negative(-10)
print(num2)
# Task4


def is_positive(number3):
    if number3 > 0:
        return True
    else:
        return False


num3 = is_positive(10)
print(num3)

# Task 5


def make_absolute(random_number):
    if random_number < 0:
        return random_number * (-1)
    else:
        return random_number


num4 = make_absolute(10)
print(num4)

# Task 6


def calculate(a, operation, b):
    operation = '+' or '-' or '*' or '/'
