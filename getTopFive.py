"""
1. Please write something that gets a list of grade in an exam, and returns the top 5 grades

2. I also need to know what are the bottom 10 grades

©Masterschool

©2025 Justus Decker - getTopFive
"""
def getTop(grades: list[int],sort:bool,l:int=5) -> list:
    "sort: True = top | False = bottom, l: length of return"
    return sorted(grades,reverse=sort)[:l]

grades = [14,51,52,63,64,2,52,68,94,34,99,64]
print(getTop(grades,True))

print(getTop(grades,False,10))
