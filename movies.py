from random import randint
import pip
pip.main(['install', "thefuzz"])
from thefuzz import fuzz
import matplotlib.pyplot as plt


"""
Living in a Movie
You're now going to start your first project 🎊
This exercise is the first step of the project. 
In the upcoming units you'll take the code that you wrote here and extend it to support additional features.

We're building a movie application. Your movie application will store movie names and their ratings.
You will communicate with the user via a command line, i.e., you print information to the terminal and expect user input.
Your application will support two types of commands:

1. CRUD - Create, Read, Update, Delete

Almost every application implements CRUD commands, since you want to add movies (Create), view the existing movies (Read), update movies (Update), and delete movies (Delete).
You can read more about CRUD in this link, or just Google it.

2. Analytics

Analytics, such as getting the top-rated movie, the least-rated movie etc.

Movie Data Structure

You will store the movies in a dictionary, provided to you in the skeleton file movies.py. 
ach key in the dictionary stores the movie name, and each value stores the movie’s rating.

Menu

When opening the application on the first time, your application should display a title of your application (for example, My Movies Database).
After the title, a menu should be displayed with the different options in your applications. 
Each menu item is printed with a number next to it. Then, the user is requested to enter a choice from the menu.

©Masterschool //\\

This is my work for a codio exam.
©2025 - Justus Decker

"""

class MovieRank:
  def __init__(self):
    self.movies = {
      "The Shawshank Redemption": 9.5,
      "Pulp Fiction": 8.8,
      "The Room": 3.6,
      "The Godfather": 9.2,
      "The Godfather: Part II": 9.0,
      "The Dark Knight": 9.0,
      "12 Angry Men": 8.9,
      "Everything Everywhere All At Once": 8.9,
      "Forrest Gump": 8.8,
      "Star Wars: Episode V": 8.7
  }
  def iterateMovies(self,cb=None):
      for key in self.movies:
            if cb is not None:
                cb(key)          
  def iterateMoviesAndRatings(self,cb=None):
      for key in self.movies:
        if cb is not None:
          cb(key,self.movies[key])
  def getMovie(self,types:str):
      _ret = []
      if "m" in types:
          _ret.append([i for i in self.movies])
      if "r" in types:
          _ret.append([self.movies[i] for i in self.movies])
      return _ret
  def update(self,inp):
    if inp == "1": #List Movies
      print(f"Movies in total: {len(self.movies)}")
      print(f"{'Movie':<35} {'Rating'}")
      self.iterateMoviesAndRatings(lambda x, y: print(f"{x:<35}: {y}"))

    if inp == "2":  #Add Movie
      title, rating =  getUserInputColorized("Movie title: "), int(getUserInputColorized("Movie rating: "))
      
      if title not in self.movies:
        self.movies[title] = rating
    if inp == "3":  #Delete Movie
      title =  getUserInputColorized("Movie title: ")
      if title in self.movies:
        self.movies.pop(title)
    if inp == "4":  #Update Movie
      title, rating =  getUserInputColorized("Movie title: "), int(getUserInputColorized("Movie rating: "))
      if title in self.movies:
        self.movies[title] = rating
    if inp == "5":  #Stats
      ratings = self.getMovie("r")[0]
      median = ratings.copy()
      median.sort()
      median = median[len(median)//2]
      average = sum(ratings) / len(ratings)
      worst, ratingW = "",11
      best, ratingB = "",-1
      for key in self.movies:
        if self.movies[key] > ratingB:
            best = key
            ratingB = self.movies[key]
        if self.movies[key] < ratingW:
            worst = key
            ratingW = self.movies[key]
    
      print(f"Average rating: {round(average,2)}. Median rating: {median}. Worst Rating: {worst} with {ratingW}/10. Best Rating: {best} with {ratingB}/10")
    if inp == "6":  #Stats
        rndMovie = [i for i in self.movies][randint(0,len(self.movies)-1)]
        print(f"{rndMovie}: {self.movies[rndMovie]}")
    if inp == "7":  #Search Movie
        value = getUserInputColorized("Search: ")
        if value in self.movies:
          print(self.movies[value])
        else:
          for movie in self.movies:
            if fuzz.ratio(value.lower(),movie.lower()) > 50:
              print(f"\033[0;33mDid you mean {movie}?\033[0m")
              break
          else:
            print("\033[0;31mNo Results!\033[0m")
    if inp == "8":  #Movie sorted by rating
        names, ratings = bubbleSort([self.movies[i] for i in self.movies],[i for i in self.movies])
        names.reverse()
        ratings.reverse()
        for r, n in zip(names,ratings):
            print(f"{n:<35}: {r}/10")
    if inp == "9":  #Create rating histogram
      plt.hist([self.movies[i] for i in self.movies])
      plt.show() 
def getUserInputColorized(msg):
  _ = input(f"{msg}\033[1;32m")
  print("\033[0m",end="")
  return _
def bubbleSort(array1,array2):
    
    n = len(array1)

    for i in range(n):
        for j in range(0, n - i - 1):

            if array1[j] > array1[j + 1]:
                array1[j], array1[j + 1] = array1[j + 1], array1[j]
                array2[j], array2[j + 1] = array2[j + 1], array2[j]
    return array1,array2

def main():
  while 1:
    print("""
********** My Movies Database **********

Menu:
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Create Rating Histogram 
    """)
    MR.update(getUserInputColorized("Enter choice 1-9: "))
    


if __name__ == "__main__":
  MR = MovieRank()
  main()
