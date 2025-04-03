"""
Prime Minister
Your goal in this exercise is to write a program that finds all the prime numbers in a given range of numbers.
We will build this program in steps, each step adding another function that use the previous one.
©Masterschool

My Codio Answer ©2025 Justus Decker
"""

def is_divisible_by(number, by):
	return number % by == 0

def is_prime(number):
    for i in range(2,number):
        if is_divisible_by(number,i):
            return False
    return True

def primes_in_range(start,end):
    for i in range(start,end):
        if is_prime(i):
            print(f"The number {i} is prime")

if __name__ == "__main__":
    primes_in_range(int(input("Enter start range: ")),int(input("Enter end range: ")))
    print(is_prime(10))
    print(is_prime(2))
    print(is_prime(13))
    print(f"Is 10 divided by 2? {is_divisible_by(10, 2)}")
    print(f"Is 10 divided by 3? {is_divisible_by(10, 3)}")
    print(f"Is 20 divided by 11? {is_divisible_by(20, 11)}")