import turtle
SNAKE = turtle.Turtle()

"""
f: foreward
r: rotate +> 0 right else left
u: pen up
d: pen down
c: color
b: backward
"""
from random import randint
def getRandomColor():
    color = hex(randint(0,16777215)).split('0x')[1]
    color = ((6-len(color)) * '0') + color
    return f"#{color}"

args = (f"f:90 b:90 r:90 c:{getRandomColor()} " * 4) + "r:1 "
args = args[:-1]

print(args)
SNAKE.speed(1000)
while 1:
    args = (f"f:90 b:90 r:90 c:{getRandomColor()} " * 4) + "r:1 "
    args = args[:-1]
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
                SNAKE.color(i[2:])



