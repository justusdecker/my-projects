"""
Built-in functions exercise
*Try to implement the following functions using built-in functions.
*Remember - There are multiple ways to implement each thing.
*Dont copy code if you can't explain it yourself!

1. A function named get_max that returns the maximum value in a list of numbers
2. A function called only_unique that gets a list and returns it without duplicates
3. A function called starts_with that checks if a string starts with another string.
4. A function called factorial to calculate the factorial of a number.
5. A function called all_equal that checks if all items of a list are identical.
"""



from math import factorial as fact
from typing import Iterable
def get_max(l:Iterable[int | float]):
    return max(l)

print(get_max([1,2,3,4,5]))

def only_unique(l: Iterable):
    return list(set([1,2,3,4,5,5,3,2,1]))

def starts_with(s:str,p:str):
    return s.startswith(p)

def factorial(n:int):
    return fact(n)
def factorial_normal(s):
    _ret = 1
    for i in range(1,s+1): _ret *= i
    return _ret
print(factorial(6))
print(factorial_normal(6))
def all_equal(l1:list,l2:list):
    return l1 == l2
print(all_equal([1,2,3],[1,2,3]))