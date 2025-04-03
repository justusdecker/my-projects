"""
Intro: Coding Standards - Classwork
Below are bad, dirty, sad, code snippets. Improve the code using everything we learned!
Guidelines
Look hard for things to improve, there may be more to fix than meets the eye!
Remember, some things are up for debate (Is a comment redundant? What name is meaningful?). If you are working in a group try to find the best solution together!
Useful resources
Your “Coding Standards Cheatsheet”
PEP8
Clean Code in Python, an article that lays out many standards and best practices.
The Zen of Python (Write import this in the interpreter).
Partial list of problems to look for
Meaningful names
No docstrings
Wrong indentation
No / too much spacing
Non ‘Pythonic' code
Redundant comments / lack of comments
A function with more than one responsibility
"""
from typing import Iterable

def categorizeAge(AGE):
    if AGE<13:
        return "Child"
    else:
        if AGE<20:
            return "Teen"
        else:
            if AGE<60:
                return "Adult"
            else:
                return "Senior"
            
def categorize_age(age:int) -> str:
    if age<13:   return "Child"
    elif age<20: return "Teen"
    elif age<60: return "Adult"
    else:        return "Senior"
print(categorize_age(18))
"""def Func1(Data):
 tmp = []
 for x in Data:
   if x%2==0:
   tmp.append(x)
 return tmp"""
def get_even_numbers(data:list[int]) -> list[int]:
    return [x for x in data if not x%2]
print(get_even_numbers([i for i in range(100)]))

def processdata(data):
    # Create empty list
    result = [   ]
    # Loop through data
    for item in data:
        # Multiply by 2
        x = item * 2
        # Append to list
        result.append(x)
    # Return result
    return result

def process_data(data:Iterable[int | float]) -> list[int]:#? Ints, floats, strings or eggs?
    return [num * 2 for num in data]
print(process_data([i for i in range(100)]))

def fnd_mx(lst):
    max_val = lst[0]
    for i in range(1, len(lst)):
      if lst[i] > max_val:
        max_val = lst[i]
    return max_val

def find_max(l:Iterable[int | float]) -> int | float:
    maximum = l[0]
    for num in l:
        if num > maximum:
            maximum = l
    return maximum

def find_max(l:Iterable[int | float]) -> int | float:
    return max(l)#tada :P
print(find_max([i for i in range(100)]))

"""def print_now_and_get_minutes_in_year(years):
		print(now.time())
    return years * 60 * 24 * 365"""
from datetime import datetime
def get_minutes_in_year(years: int | float) -> int | float:
    return years * 60 * 24 * 365
print(datetime.now())
print(get_minutes_in_year(25.25))


def lol(numbers):
    out = []
    for l in numbers:
        if l>= 2:
            #good flag
            notgood = False
            #chaeck if prime
            for i in range(2,l):
                if l % i == 0:
                    notgood=True; break
            if not notgood:
                out.append(l)
    return out
from functools import lru_cache
@lru_cache
def is_prime(number):
    for i in range(2,number):
        if number % i == 0: return False
    return True

def get_primes(r:Iterable[int]):
    return [l for l in r if is_prime(l) and l >= 2]
print(get_primes((5,2,6,1,6,4,3,7)))



def A(p,n=10):
    """
    Analyze word frequency in a text file.
    Args:
        p (str): Path to the text file
        n (int): Number of top frequent words to return
    
    Returns:
        list: Top N most frequent words with their counts
    """
    z={}
    try:
        f=open(p,'r')
        t=f.read().lower()
        f.close()
        w=t.split()
        for x in w:
            x=x.strip('.,!?():;[]"\'')
            if x!='':
                if x in z:z[x]+=1
                else:z[x]=1
        
        y=list(z.items())
        for m in range(len(y)):
            for k in range(0, len(y)-m-1):
                if y[k][1] < y[k+1][1]:
                    y[k], y[k+1] = y[k+1], y[k]
        return y[:n]
    except:
        return "err"
from os import path

def bubble_sort(array1,array2):
    
    n = len(array1)

    for i in range(n):
        for j in range(0, n - i - 1):
            if array1[j] > array1[j + 1]:
                array1[j], array1[j + 1] = array1[j + 1], array1[j]
                array2[j], array2[j + 1] = array2[j + 1], array2[j]
    return array1,array2

def get_word_frequency(file_path:str):
    cache = {}
    data = []
    if path.isfile(file_path):
        with open(file_path,"rb") as f_in:
            data = "".join([chr(char) for char in f_in.read() if str(char).isascii()]).lower().split()
    for word in data:
        if word:
            if word in cache: 
                cache[word] += 1
            else: 
                cache[word]=1
                
    return bubble_sort(list(cache.values()),list(cache.keys()))
print(get_word_frequency("win_act.bat"))