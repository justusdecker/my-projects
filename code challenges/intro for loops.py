"""
### 1: Name Printer

Write a program that:

- Creates a list of names
- Uses a for loop to print each name with a message.
- Bonus - Prints a special message when a specific name is found

---

### 2: Vowel Counter Function

Create a function that:

- Counts vowels in a given text string
- Uses a for loop
- Returns the total number of vowels

### 3: Pass or Fail

Write a function that:

- Takes a list of Grades
- Calculates total score
- Determines pass/fail status (passing grade is average equal to or higher than 70)

---

### 4: Number Processing with Break and Continue

Create a function that:

- Processes a list of numbers
- Skips negative numbers using continue
- Stops processing if number exceeds 100 using break
- Calculates total of valid numbers

### Bonus: Complex Word Filter

Develop a function that:

- Takes a list of words
- Counts words longer than 5 characters
- Stops counting if a word longer than 10 characters is found
- Returns the count of eligible words

©Masterschool

©2025 Justus Decker
"""

from random import randint

#Challenge 1 - A bit more complex :D
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



#Challenge 2
def vowelCounter(text:str):
    text = text.lower()
    return sum([text.count(char) for char in "aeiou"])

print(vowelCounter("A vowel is a speech sound pronounced without any stricture in the vocal tract, forming the nucleus of a syllable."))

#Challenge 3
grades = [randint(35,100) for i in range(15)]
total = sum(grades)
passed = len([i for i in grades if i >= 70])
avg = total / len(grades)
print(f"{(passed/len(grades))*100:.2f}% passed the test. In total: {total} students. Average: {avg:.2f}%")

#Challenge 4
_sum = 0
for i,idx in enumerate([randint(-25,25) for i in range(32)]):
    if i < 0: continue
    if _sum > 100: break
    _sum += i
print(f"Result: {_sum} takes {idx+1} iterations")

#Bonus


text = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
def legal(text:str) -> int:
    
    count = 0
    for word in text.split(" "):
        l = len(word)
        if l > 5: count += 1
        if l > 10: break
    return count
print(legal(text))