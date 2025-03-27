"""
(c) Masterschool
(c) 2025 - Coding solution by Justus Decker

Refactor Goldbach's Conjecture
In this exercise, you’ll implement what you learned in Coding Standards lesson, and make sure all of your future code is written according the best standards.
Goldbach’s Conjecture
Goldbach’s conjecture is one of the oldest and best-known unsolved problems in number theory and all of mathematics. It states that every even natural number greater than 2 is the sum of two prime numbers.
The conjecture has been shown to hold for many numbers, but remains unproven despite considerable effort.
Example
The number 100 follows Goldbach’s conjecture, since it’s the sum of 3 and 97, and it’s the sum of 11 and 89, all of these are prime numbers.
Are we going to prove it?
Luckily, you are not. If you can solve it, you would win $1M prize!
Algorithm
Given an number number, we would like to check if it a sum of two prime numbers, x and y.
There are multiple approaches for this, we will choose one:
For each number i in range(2, x):
Check if i is a prime number.
If not, continue to the next i in the range.
Otherwise, check if number - i is prime.
If the answer is true, i and number - i are the numbers we are looking for.
Let’s see an example, for the number 100.
We are going over all the numbers from 2 to 99, setting i in each iteration:
i = 2
Check if i = 2 is a prime number.
The answer is yes, so check if number - i = 100 - 2 = 98 is a prime number.
The answer is not, since 98 is not a prime number, then continue to next i.
i = 3
Check if i = 3 is a prime number.
The answer is yes, so check if number - i = 100 - 3 = 97 is a prime number.
The answer is yes, since 97 is a prime number, then 3 and 97 are the numbers we’re looking for.
i = 4
Check if i = 4 is a prime number.
The answer is no, so continue to next i.
…
Refactoring Assignment
On the right, you have a code that tests Goldbach’s conjecture for a number that the user inputs. The code
This is not a good code. While it is working, it doesn’t follow PEP 8 guidelines, and it have a poor division to functions. It’s very hard to read.
You need to refactor the code to make it perfect.
What is code refactoring?
Code refactoring is the process of modifying existing source code to improve its readability, maintainability, and/or performance, without changing its external behavior. This involves restructuring the code’s internal structure and organization, while preserving its overall functionality.
How do I start?
First of all, run the code and see what it does.
After that, go back to Coding Standards lesson and the Coding Standards Cheat Sheet. We highly recommend coding in PyCharm, since it has a built-in PEP 8 style checker.
Specifically, pay attention to these points:
Naming
Division to functions
Spacing
Unnecessary parenthesis
More things you can find!
After you refactor the code, make sure it’s working properly.
"""

def is_prime(number:int) -> bool:
    return [(number-1)%n for n in range(1,number)].count(True) == 1
def short_sotp(number):
    """
    My own list comprehension solution. Does the same as sum_of_two_primes!
    """
    already_used: list = []
    for result in [[[i,j] for j in range(number - i,number) if is_prime(j) and i + j == number] for i in range(2,number) if not number%2 and is_prime(i) and number - i >= 2]:
        if result:
            result[0].sort()
            if result[0] not in already_used:
                already_used.append(result[0])
    return already_used

def sum_of_two_primes(number):
    if number%2: return
    already_used: list = []
    for i in range(2,number):
        second = number - i
        if is_prime(i) and second >= 2:
            for j in range(second,number):
                if is_prime(j) and i + j == number:
                    result = [i,j]
                    result.sort()
                    if result not in already_used:
                        already_used.append(result)
    return already_used

def check_user_input_until_integer(prompt:str) -> str:
    user_input: str = ""
    while not user_input:
        user_input = input(prompt)
        user_input = user_input if user_input.isdecimal() else ""
    return user_input

number = int(check_user_input_until_integer("Enter a number: "))

for a,b in sum_of_two_primes(number):
    print(f"The number {number} equals to the sum of {a} and {b}")
    
for a,b in short_sotp(number):
    print(f"The number {number} equals to the sum of {a} and {b}")