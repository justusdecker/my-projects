"""
Please write something that gets a list of grade in an exam, and returns the top 5 grades
©Masterschool

©2025 Justus Decker - getTopFive
"""
def getTopFive(grades: list | tuple) -> list:
    grades.sort(), grades.reverse()
    return grades[:5]
grades = [14,51,52,63,64,2,52,68,94,34,99,64]
print(getTopFive(grades))