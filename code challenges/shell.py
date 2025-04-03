"""
## **🧡 Mini Challenge #1**

You are working in a school, and you’re given a list of all grades in an exam.

Copy

`grades = [10, 50, 60, 10, 50, 60, 30, 50]`

1. Copy this list and paste it into the interactive shell.
2. Type `print(grades)` and see that you see the list of grades.
3. Type only `grades` and verify that you got the same result.
    1. In the interactive shell, you don’t need to `print`, as opposed to a regular file where you always have to print.

### Assignment

1. Print only the grades that passed the exam, i.e., got a grade above 60.
2. Print “PASSED” for grades that have passed and “FAILED” for the rest, along with the grade itself.
3. Print the grades with added 10% to every grade.

## **💛 Mini Challenge #2**

You got a list of websites:

Copy

`websites = ["google.com", "youtube.com", "facebook.com", "twitter.com", "instagram.com", "baidu.com", "wikipedia.org","yandex.ru", "yahoo.com"]`

1. Print only the websites that end with .com.
2. Print all the websites with .net instead of .com.
3. Print only the website name capitalized without the extension (Output: Wikipedia, Twitter…).

## **💙 Mini Challenge #3**

Explore libraries with the Python interactive shell.

1. Import the `random` module to the interactive shell by typing `import random`.
2. View the functions inside the module by typing `dir(random)`.
3. Choose a function that seems interesting to you. For example, [`random.foo`](http://random.foo/) (this function doesn’t really exist).
4. Use the `help` command to read the documentation (in the interpreter) about the function: `help(random.foo)`.
5. After you finish reading the documentation, you may need to press `q` to exit it.
6. Use the information that you read and use the function, to explore it.
7. Feel free to explore more functions!
©Masterschool

©2025 Justus Decker
"""
#Mini Challenge 1

grades = [10, 50, 60, 10, 50, 60, 30, 50]

for grade in grades:
    if grade > 60:
        print("PASSED!")
    else:
        print("FAILED!")
    print(int(grade*1.1))

#Mini Challenge 2
websites = ["google.com", "youtube.com", "facebook.com", "twitter.com", "instagram.com", "baidu.com", "wikipedia.org","yandex.ru", "yahoo.com"]

for ws in websites:
    if ws.endswith(".com"):
        splitted_ws = ws.split('.')
        print(splitted_ws)
        new_ws = splitted_ws[0] + ".net"
        print(new_ws)
    splitted_ws = ws.split('.')
    print(splitted_ws[0].capitalize())


#Mini Challenge 3

import random
from random import randint
print(dir(random))
print(randint.__doc__,help(randint))
print(randint(-15,15))
