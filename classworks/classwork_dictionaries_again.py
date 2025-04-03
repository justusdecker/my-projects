"""
Intro: Dictionaries - Classwork
(c) Masterschool
(c) 2025 - Justus Decker - My solution
1️⃣: Cinema Manager 🍿 
You’re building a program for a movie theater and need to create a dictionary to store the movies and their respective ticket prices.
    1.  Create a dictionary called movies_prices where the keys are movie titles and the values are ticket prices. Use these movies: "Inception" (12), "Avatar" (15), "Moana" (8)
    2.  Add a new movie of your choice with a price.
    3.  Change the price of "Inception" to 10.
    4.  Print only the movie titles.
    5.  Print the full menu in a readable way, e.g., "Inception - $10".  (hint - use an f string)
 
2️⃣: Cinema Manager - The Return 🎬
Now, let’s extend your cinema manager program by adding some functionality with functions to make it more interactive and dynamic.
    1.  Define a function add_movie() that takes in a movie title and price, and adds the movie to the movies_prices dictionary. If the movie already exists, it should print a message saying that the movie is already there. Example input: "The Matrix", 10
    2.  Define a function update_price() that allows you to update the price of an existing movie. It should take the movie title and the new price as arguments. If the movie doesn't exist, it should print a message saying that the movie is not found.
    3.  Define a function get_ticket_price() that takes a movie title as input and returns the price of the movie. If the movie doesn’t exist in the dictionary, return "Movie not found!".
    4.  Define a function remove_movie() that removes a movie from the movies_prices dictionary by title.

3️⃣: Student Grade Calculator 📊 
You are building a student grade tracker. With student names as keys and list of grades as values.
Copy this dictionary student_grades.
student_grades = {
    "emma_schneider": [88, 92, 79],
    "jonas_muller": [76, 81, 85],
    "ben_fischer": [90, 87, 93],
    "felix_wagner": [72, 75, 70],
    "lena_hoffmann": [95, 89, 91]
}
    1.  Calculate and print the best grade for each student. The best grade is the highest grade in the list for that student.
    2.  Calculate and print the average grade for each student across all subjects, rounded down to the nearest whole number, e.g, 86.7 → 86 (hint: use builtin list operations)
    3.  Create a function find_top_student(student_grades) that.
            Accepts the dictionary student_grades.
            Returns the name of the student with the highest average grade.
 
"""

print("1️⃣ & 2️⃣: Cinema Manager 🍿 ")
class Movie:
    MSG_KEY_DOES_NOT_EXIST = "This movie does not exist"
    MSG_IS_NOT_DECIMAL = "The price isn't decimal"
    MSG_MOVIE_ALREADY_EXISTS = "movie is already in the cinema"
    def __init__(self):
        self.movies: dict = {"Inception":12,"Avatar":15,"Moana":8}
    def is_decimal(self,key:str) -> bool:
        if not key.isdecimal(): print(self.MSG_IS_NOT_DECIMAL)
        return key.isdecimal()
    def chk_in(self,key:str) -> bool:
        if not key in self.movies: print(self.MSG_KEY_DOES_NOT_EXIST)
        return key in self.movies
    def add_movie(self,title:str,price:str):
        if title in self.movies:
            print(self.MSG_MOVIE_ALREADY_EXISTS)
            return 
        if not self.is_decimal(price): return
        self.movies[title] = int(price)
    def remove_movie(self,title:str):
        if not self.chk_in(title): return
        self.movies.pop(title)
    def get_ticket_price(self,title:str):
        if not self.chk_in(title): return
        return self.movies[title]
    def update_price(self,title:str,price:str):
        if not self.is_decimal(price) or not self.chk_in(title): return
        self.movies[title] = int(price)

print("3️⃣: Student Grade Calculator 📊 ")
student_grades = {
    "emma_schneider": [88, 92, 79],
    "jonas_muller": [76, 81, 85],
    "ben_fischer": [90, 87, 93],
    "felix_wagner": [72, 75, 70],
    "lena_hoffmann": [95, 89, 91]
}
for student in student_grades: print(max(student_grades[student]))
for student in student_grades: print(max(student_grades[student]) / len(student_grades[student]))

def find_top_student(student_grades):
    students = [student for student in student_grades]
    grades = [max(student_grades[student]) / len(student_grades[student]) for student in student_grades]
    best = max(grades)
    return students[grades.index(best)],grades[grades.index(best)]

print(find_top_student(student_grades))
