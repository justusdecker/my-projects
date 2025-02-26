"""
Intro: Dictionaries - Classwork
Exercise 1: Cinema Manager 🍿 
You’re building a program for a movie theater and need to create a dictionary to store the movies and their respective ticket prices.
Create a dictionary called movies_prices where the keys are movie titles and the values are ticket prices. Use these movies: "Inception" (12), "Avatar" (15), "Moana" (8)
Add a new movie of your choice with a price.
Change the price of "Inception" to 10.
Print only the movie titles.
Print the full menu in a readable way, e.g., "Inception - $10".  (hint - use an f string)
 
Exercise 2: Cinema Manager - The Return 🎬
Now, let’s extend your cinema manager program by adding some functionality with functions to make it more interactive and dynamic.
Define a function add_movie() that takes in a movie title and price, and adds the movie to the movies_prices dictionary. If the movie already exists, it should print a message saying that the movie is already there.
Example input: "The Matrix", 10
Define a function update_price() that allows you to update the price of an existing movie. It should take the movie title and the new price as arguments. If the movie doesn't exist, it should print a message saying that the movie is not found.
Define a function get_ticket_price() that takes a movie title as input and returns the price of the movie. If the movie doesn’t exist in the dictionary, return "Movie not found!".
Define a function remove_movie() that removes a movie from the movies_prices dictionary by title.
 
Exercise 3: Student Grade Calculator 📊 
You are building a student grade tracker. With student names as keys and list of grades as values.
Copy this dictionary student_grades .
Copied code
to clipboard
1234567
student_grades = {
    "emma_schneider": [88, 92, 79],
    "jonas_muller": [76, 81, 85],
    "ben_fischer": [90, 87, 93],
    "felix_wagner": [72, 75, 70],
    "lena_hoffmann": [95, 89, 91]
}
Calculate and print the best grade for each student. The best grade is the highest grade in the list for that student.
Calculate and print the average grade for each student across all subjects, rounded down to the nearest whole number, e.g, 86.7 → 86 (hint: use builtin list operations)
Create a function find_top_student(student_grades) that:
Accepts the dictionary student_grades.
Returns the name of the student with the highest average grade.
©Masterschool

©2025 Justus Decker
"""

moviePrices = {
    'Inception': 12,
    'Avatar': 15,
    'Moana': 8
}

moviePrices['Robin Hood'] = 17
moviePrices['Inception'] = 10

for movie in moviePrices:
    print(movie)
    
for movie in moviePrices:
    print(f"{movie:<15}:{moviePrices[movie]}")
    

def addMovie(title,price):
    if title in moviePrices:
        print("Movie already exists")
        return
    moviePrices[title] = price
def updatePrice(title,price):
    if title in moviePrices:
        moviePrices[title] = price
    else:
        print("Movie not in Dict!")
def removeMovie(title):
    if title in moviePrices:
        moviePrices.pop(title)
    else:
        print("Movie not in Dict!")
def getTicketPrice(title):
    if title in moviePrices:
        return moviePrices[title]
    else:
        print("Movie not in Dict!")
        return 0
    
student_grades = {
    "emma_schneider": [88, 92, 79],
    "jonas_muller": [76, 81, 85],
    "ben_fischer": [90, 87, 93],
    "felix_wagner": [72, 75, 70],
    "lena_hoffmann": [95, 89, 91]
}

for student in student_grades:
    print(f"{student} best grade: {max(student_grades[student])}. Average: {round(sum(student_grades[student]) / len(student_grades[student]),2)}")
student = ''
m = 0
for student in student_grades:
    s = round(sum(student_grades[student]) / len(student_grades[student]),2)
    if m < s:
        student = student
        m = s
print(f"Best student {student}: {m}")
