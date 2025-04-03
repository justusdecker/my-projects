"""
(c) Masterschool
(c)2025 Justus Decker - My solution
"""

"""
Exercise 1: Handling Division Errors  🧮
The following code throws an exception:

Run the program and note the exception type. What type is it?
Try to make the program crash-proof using conditionals (if/else statements). [NOPE]
Try to make the program crash-proof using try/except/finally (Don't use the generic Exception).
Which of the two methods do you prefer and why?

"""
def is_divisible_by(number, divisor):
    try:
        return number % divisor == 0
    except TypeError:
        return 0
    except ZeroDivisionError:
        return 0

print(is_divisible_by(10, 2))
print(is_divisible_by(10, "2"))  # TypeError
print(is_divisible_by(10, 0))  # ZeroDivision

"""
Exercise 2: Fixing Percentage Calculation Errors  🏦
The following function adds a percentage to a price:

Run the program and note the exception type. What type is it?
Try to make the program crash-proof using conditionals (if/else statements). [NOPE]
Try to make the program crash-proof using try/except/finally (Don't use the generic Exception).
"""

def add_percentage(price, percentage):
    try:
        return price + (percentage * price)
    except TypeError:
        return price

print(add_percentage(100, 0.1))
print(add_percentage(100, "0.05"))  # Causes an exception

"""
Exercise 3: Fixing Student Grade Lookup  🎓
XYZ School’s program crashes if there’s a typo in the student’s name:

Could you help XYZ school make the program crash-proof by catching the exception and displaying a message to the teachers?
XYZ school will also like to search the database using all lower-case student names. e.g. "John" and "john" should be treated as the same student. Update the program to meet this requirement.
"""

def get_grade(database, student_name:str):
    database = {key.lower(): database[key] for key in database}
    if student_name.lower() in database: return database[student_name.lower()]
    else:
        print("Student name is not in database!")
        return ""

db = {"John": "A+", "Mary": "B", "Jane": "C", "Thomas": "B+"}

name = "John"
print(get_grade(db, name))  # Works fine
name = "Johnn"
print(get_grade(db, name))  # Causes an exception

"""
Bonus Exercise  💪
The following function calculates the square of a number:

Update the function. Raise one exception for each of the following cases:
A user enters a string.
A user enters a negative number.
A user enters a number less than 1 or greater than 100.
Call the function inside a try/except block. Ensure you catch all the exceptions raised (Do not use the generic Exception).
"""
def calculate_square(number):#DEFAULT
    return number * number

def convert_to_float(text:str) -> bool | float:
    """
    Return the float: convert is possible
    Return False: Error occured
    """
    if text.count(".") == 0 and text.isdecimal():
        return float(text)
    if text.count(".") == 1 and text != '.':
        a,b = text.split(".")
        if a + b == 2: raise TypeError("strings are not valid!")
        return float(f"{a + '.' if a.isdecimal() else '0.'}{b if b.isdecimal() else '0'}")
    raise TypeError("strings are not valid!")

def calculate_square(number): # NEW
    
    number = convert_to_float(str(number))
    if number > 100 or number < 1: raise ValueError("number is not in range")
    return number ** 2
print(calculate_square(12))