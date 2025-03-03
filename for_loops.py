from random import randint
from typing import Iterable
users = [
    {
        "name": "Justus Decker",
        "street": "Bahnhofsstraße",
        "houseNumber": 13,
        "postalCode": "26725",
        "city": "Emden",
        "federalState": "lower Saxony"
    },
    {
        "name": "Pia Nova",
        "street": "Polderweg",
        "houseNumber": 45,
        "postalCode": "26721",
        "city": "Emden",
        "federalState": "lower Saxony"
    },
    {
        "name": "Tim Osterburg",
        "street": "Tinsdaler Heideweg",
        "houseNumber": 11,
        "postalCode": "22559",
        "city": "Hamburg",
        "federalState": "hamburg"
    }
]

for user in users:
    print(f"{user['name']} sedentary in {user['street']} {user['houseNumber']} | {user['postalCode']} in {user['city']} ({user['federalState']})")




#!create an array of 32 integer in random range from 1-64. The sum will be printed!
#Compact, Simple & easy to read.
print(sum([randint(1,64) for i in range(32)]))

"""
Create a list. print the number of each element
Create a list. print the number squared! of each element
©Masterschool

©2025 Justus Decker
"""


def sort(unsortedList:Iterable) -> Iterable:
    """
    Title: ...
    Type: Sorting algorithm
    Time complexity: O(n^2)
    """
    for j in range(len(unsortedList)-1):
        for i in range(len(unsortedList)-1):
            a,b = unsortedList[i],unsortedList[i+1]
            if a > b:
                unsortedList[i] = b
                unsortedList[i+1] = a
                
    return unsortedList
numbers = [randint(1,64)**2 for i in range(32)]
print(sort(numbers))

print(sum(numbers)) # OR

numberSum = 0
for i in numbers:
    numberSum += i
print(numberSum)

