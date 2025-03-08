from random import randint
import pip
try:
    from thefuzz import fuzz
except Exception as E:
    print("Module not found!")
    pip.main(['install', "thefuzz"])
finally:
    from thefuzz import fuzz
import matplotlib.pyplot as plt
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
  def update(self,inp):
    if inp == "1":
      print(f"Movies in total: {len(self.movies)}")
      print(f"{'Movie':<25} {'Rating':<7}")
      for key in self.movies:
        print(f"{key:<25} {self.movies[key]:<7}")
    if inp == "2":
      title, rating =  getUserInputColorized("Movie title: "), int(getUserInputColorized("Movie rating: "))
      
      if title not in self.movies:
        self.movies[title] = rating
    if inp == "3":
      title =  getUserInputColorized("Movie title: ")
      if title in self.movies:
        self.movies.pop(title)
    if inp == "4":
      title, rating =  getUserInputColorized("Movie title: "), int(getUserInputColorized("Movie rating: "))
      if title in self.movies:
        self.movies[title] = rating
    if inp == "5":
      ratings = [self.movies[i] for i in self.movies]
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
    if inp == "6":
        rndMovie = [i for i in self.movies][randint(0,len(self.movies)-1)]
        print(f"{rndMovie}: {self.movies[rndMovie]}")
    if inp == "7":
        value = getUserInputColorized("Search: ")
        if value in self.movies:
          print(self.movies[value])
        else:
          for movie in self.movies:
            if fuzz.ratio(value,movie) > 85:
              print(f"Did you mean {movie}?")
          else:
            print("\033[0;31mNo Results!\033[0m")
    if inp == "8":
        names, ratings = bubbleSort([self.movies[i] for i in self.movies],[i for i in self.movies])
        names.reverse()
        ratings.reverse()
        for n, r in zip(names,ratings):
            print(f"{n}: {r}/10")
    if inp == "9":
      plt.hist([self.movies[i] for i in self.movies])
      plt.show() 
def getUserInputColorized(msg):
  _ret = input(f"{msg}\033[1;32m")
  print("\033[0m",end="")
  return _ret #!Bugfix: The value has to be an string not NoneType
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
    print("""\033[J
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
    
    getUserInputColorized("Press Enter to continue")


if __name__ == "__main__":
  MR = MovieRank()
  main()
