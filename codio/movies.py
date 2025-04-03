from random import randint
import pip
__version__ = "1.2"
try:
    from thefuzz import fuzz
except Exception as E:
    print("Module not found!")
    pip.main(['install', "thefuzz"])
finally:
    from thefuzz import fuzz
import matplotlib.pyplot as plt

"""
Changed the if hell in updates to match&case
Changed to snail_case instead of camelCase!
Fixed search method. Now: text converts to lowercase and then compare
The program give the user information like: "This movie doesn't exist"
Fixed the median calculation in stats.
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
    def update(self,inp):
        match inp:
            case "1":#$Show all movies in a table
                print(f"Movies in total: {len(self.movies)}")
                print(f"{'Movie':<25} {'Rating':<7}")
                for key in self.movies:
                    print(f"{key:<25} {self.movies[key]:<7}")
            case "2":#$Add new movie
                title =  get_user_input_colorized("Movie title: ")
                rating = convert_to_float(get_user_input_colorized("Movie rating: "))
                if not rating: 
                    print("\033[0;31mRating is not a number!\033[0m")
                    return
                if title not in self.movies:
                    self.movies[title] = rating
            case "3":#$remove existing movie
                title =  get_user_input_colorized("Movie title: ")
                if title in self.movies:
                    self.movies.pop(title)
                else:
                    print("\033[0;31mThis movie doesn't exist\033[0m")
            case "4":#$edit movie
                title =  get_user_input_colorized("Movie title: ")
                rating = get_user_input_colorized("Movie rating: ")
                if not rating: 
                    print("\033[0;31mRating is not a number!\033[0m")
                    return
                
                if title in self.movies:
                    self.movies[title] = rating
                else:
                    print("\033[0;31mThis movie doesn't exist\033[0m")
            case "5":
                ratings = [self.movies[i] for i in self.movies]
                median = ratings.copy()
                median.sort()
                median_hlen = len(median)//2
                if len(median) % 2:
                    median = median[median_hlen]
                else:
                    
                    _median_1 = median[median_hlen]
                    median.sort(reverse=True)
                    median = round((median[median_hlen] +_median_1) / 2,2)
                    print(median)
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
            case "6":
                rndMovie = [i for i in self.movies][randint(0,len(self.movies)-1)]
                print(f"{rndMovie}: {self.movies[rndMovie]}")
            case "7":#$Search
                value = get_user_input_colorized("Search: ").lower()
                if value in self.movies:
                    print(self.movies[value])
                else:
                    for movie in self.movies:
                        if fuzz.ratio(value,movie.lower()) > 85:
                            print(f"Did you mean {movie}?")
                    else:
                        print("\033[0;31mNo Results!\033[0m")
            case "8":
                names, ratings = bubble_sort([self.movies[i] for i in self.movies],[i for i in self.movies])
                names.reverse()
                ratings.reverse()
                for n, r in zip(names,ratings):
                    print(f"{r}: {n}/10")
            case "9":
                plt.hist([self.movies[i] for i in self.movies])
                plt.show()
            case _:
                print("\033[0;31mInvalid Input!\033[0m")
                
def convert_to_float(text:str) -> bool | float:
    """
    Return the float: convert is possible
    Return False: Error occured
    """
    if text.count(".") == 0 and text.isdecimal():
        return float(text)
    if text.count(".") == 1 and text != '.':
        a,b = text.split(".")
        if a + b == 2: return False #Is not a float
        return float(f"{a + '.' if a.isdecimal() else '0.'}{b if b.isdecimal() else '0'}")
    return False
def get_user_input_colorized(msg):
    _ret = input(f"{msg}\033[1;32m")
    print("\033[0m",end="")
    return _ret

def bubble_sort(array1,array2):
    
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

        MR.update(get_user_input_colorized("Enter choice 1-9: "))
    
        get_user_input_colorized("Press Enter to continue")


if __name__ == "__main__":
    MR = MovieRank()
    main()
