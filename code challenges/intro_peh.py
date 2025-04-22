def is_divisible_by(number, divisor): return (not (number % divisor)) if not (not isinstance(number,int) or not isinstance(divisor,int)) and not (not number or not divisor) else False #checks for both nums: Is int & not 0. Normally it returns the modulo of both nums.

def is_divisible_by_tes(num,div):
    try:
        return not (num % div)
    except TypeError as E:
        return False

    
print(is_divisible_by(10, 2))
print(is_divisible_by(10, "2"))  # Fixed

print(is_divisible_by_tes(10, 2))
print(is_divisible_by_tes(10, "2"))  # Fixed

def add_percentage(price, percentage):
    try:
        return (price + (percentage * price))
    except TypeError:
        return price
~2
print(add_percentage(100, 0.1))
print(add_percentage(100, "0.05"))  # Causes an exception

def get_grade(database:dict, student_name:str):
    return database.get(student_name,'')

db = {"John": "A+", "Mary": "B", "Jane": "C", "Thomas": "B+"}

name = "John"
print(get_grade(db, name))  # Works fine
name = "Johnn"
print(get_grade(db, name))  # Causes an exception


def calculate_square(n):
    if not isinstance(n,int): return 0
    if 100 <= n or n <= 0: return 0
    n = abs(n)
    return n * n
print(calculate_square(5))
print(calculate_square(7))
print(calculate_square(101))