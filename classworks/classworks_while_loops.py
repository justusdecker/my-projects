
animals = ["Hamster","Vogel","Hund","Meerschweinchen"]
for animal in animals: print(animal)

index = 0
while index < len(animals): 
    print(animals[index])
    index += 1

"""
Intro: While Loops - Classwork (c) Masterschool
Solution by Justus Decker (c) 2025

Solve the following challenges using while loops in Python.
Use Pycharm or an online IDE, e.g., https://www.online-python.com/ to do your coding
 
1️⃣ Find out when a user enters an even number
Write a program that repeatedly asks a user to input a number. Stop if the user enters an even number.

2️⃣ Four odd numbers
Write a program that repeatedly asks a user to input numbers. Stop when the user enters exactly 4 odd numbers.

3️⃣ Restaurant menu ordering
A restaurant menu contains only 3 items: fish, chips, and bread.
Write a program that repeatedly prompts a user to place an order. Stop and print a message saying “Order successfully placed” once a user enters any of the 3 items on the menu.

🔶 BONUS: Transform username
Write a program that repeatedly prompts a user for their email address. Stop if the email address is valid. An example of a valid email address is user123@mail.com or user123@mail.net
Email prefix of at least 5 characters e.g. user123
Contains @ symbol.
Domain e.g., mail.net or mail.com
"""

challenge_title = '[1️⃣ Find out when a user enters an even number]'
print(challenge_title)

user_input: str = ""
while not user_input:
    user_input = input("Enter your number: ")
    if not user_input.isdecimal():
        print("This is not a number!")
        user_input: str = ""
        continue
    
    if not int(user_input) % 2:
        print("Your number is even!")
        break
    print("Your number is odd! Try again!")
    user_input: str = ""
    
challenge_title = '[2️⃣ Four odd numbers]'
print(challenge_title)

user_input: str = ""
odd_numbers: int = 0
while not user_input:
    user_input = input("Enter your number: ")
    if int(user_input) % 2:
        odd_numbers += 1
        print(f"Your number is odd! {4-odd_numbers} left")
    else:
        print(f"Your number is event! Try again!")
    if odd_numbers >= 4:
        print(f"You reached the 4 odd numbers!")
        break
    user_input: str = ""

challenge_title = '[3️⃣ Restaurant menu ordering]'
print(challenge_title)

menu : list = ["fish","chips","bread"]
user_input: str = ""

while not user_input:
    user_input = input("Enter your order: ")
    if user_input.lower() in menu:
        print(f"Order successfully placed: [{user_input}]")
        break
    user_input: str = ""

challenge_title = '[🔶 BONUS: Transform username]'
print(challenge_title)

user_input: str = ""
invalid_msg: str = "Your E-Mail is invalid: "

while not user_input:
    user_input = input("Enter your E-Mail: ")
    if "@" not in user_input:
        print(invalid_msg + "Missing '@'")
        user_input: str = ""
        continue
    if not any([user_input.endswith(f"mail.{suffix}") for suffix in ("net","com")]):
        print(invalid_msg + "suffix is invalid")
        user_input: str = ""
        continue
    if len(user_input.split("@")[0]) < 5:
        print(invalid_msg + "length is below 5")
        user_input: str = ""
        continue
    print("Your E-Mail is valid!")
    break