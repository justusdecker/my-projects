"""
I got the same coding challenge again so i refactor & optimize this code even further

🐢 Turtle Art Challenge: Nested Loops Edition 🎨

### **Your Task**

Go to https://trinket.io/turtle:

Use **nested loops** with Python’s `turtle` module to create **interesting visual patterns**. Your designs can be geometric, abstract, or inspired by nature! 🌿✨

Think about how **loops** can help repeat shapes efficiently. Try experimenting with:


    🐢

    ✅ **Turning angles** (e.g., `.left()`, `.right()`)

    ✅ **Pen movements** (e.g., `.forward()`, `.backward()`, `.penup()`, `.pendown()`)

    ✅ **Changing colors and pen size** (`.pencolor()`, `.fillcolor()`, `.pensize()`)

    ✅ **Circles** (`.circle()`)



🚀 **Challenge Yourself!**

- Use a nested loop to **create a pattern inside a pattern**
- Experiment with **color changes** in each loop iteration
- Try using **randomization** for dynamic effects 🎲
"""

import turtle
SNAKE = turtle.Turtle()
SNAKE.speed(1000)
__doc__ = """
        f: foreward [INT]
        r: rotate > 0 right else left [INT]
        u: pen up
        d: pen down
        c: color [INT]
        v: backward [INT]
"""
class UnknownArgumentExeption(Exception):
    f"""
    Unknown argument: please read the docs:
    {__doc__}
    """
class ArgumentSyntaxExeption(Exception):
    f"""
    Wrong Argument Syntax: please read the docs:
    {__doc__}
    """
from random import randint
def getRandomColor():
    color = hex(randint(0,16777215)).split('0x')[1]
    color = ((6-len(color)) * '0') + color
    return f"#{color}"

def check_arguments(args:str):
    if args[-1].isspace():
        args = args[:-1]
    for arg in args.split(" "):
        if arg[0] not in (i for i in "fvrcud"):
            raise UnknownArgumentExeption(arg)
        if len(arg) > 3:
            if arg[0] in (i for i in "fvrc") and (not arg[2:].isdecimal() and arg[2:] != "rnd"):
                raise ArgumentSyntaxExeption(arg)
    return args
                    
                    
            
def draw(args:str):
    while 1:
        for i in args.split(" "):
            match i[0]:
                case "f":
                    SNAKE.forward(int(i[2:]))
                case "v":
                    SNAKE.backward(int(i[2:]))
                case "r":
                    if int(i[2:]) >= 0:
                        SNAKE.right(abs(int(i[2:])))
                    else:
                        SNAKE.left(abs(int(i[2:])))
                case "u":
                    SNAKE.penup()
                case "d":
                    SNAKE.pendown()
                case "c":
                    if i[2:] == "rnd":
                        SNAKE.color(getRandomColor())
                    else:
                        SNAKE.color(int(i[2:]))

draw(check_arguments(((f"f:90 r:90 c:rnd " * 4) + "r:1 ")))
#draw(check_arguments(input(f"{__doc__}\n cmd: ")))




