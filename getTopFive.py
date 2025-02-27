"""
1. Please write something that gets a list of grade in an exam, and returns the top 5 grades

2. I also need to know what are the bottom 10 grades

©Masterschool

©2025 Justus Decker - getTopFive
"""
def getTop(grades: list[int]) -> list:
    """
    reverse
    """
    return sorted(grades,reverse=True)[:5]
    
def getWorst(grades: list[int]) -> list:
    return sorted(grades)[:10]
grades = [14,51,52,63,64,2,52,68,94,34,99,64]
print(getTop(grades))
print(getWorst(grades))
