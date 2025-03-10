
"""
(c)Masterschool "Challenges"
(c)2025 Justus Decker
"""
def only_odd_nums_broken(numbers):
    for num in numbers:
        if num % 2 == 0:#If num is even.
            return False
        else:
            return True
    return True

def only_odd_nums(numbers):
    for num in numbers:
        if num % 2 == 0:#Num is even. Return early!
            return False
        #The Program should not returning if odd numbers in list.
    return True

def my_solution_only_odd_nums(numbers:list[int]) -> bool:
    return all([num % 2 for num in numbers])
list_numbers = [1,3,6]
print(my_solution_only_odd_nums(list_numbers))

def check_string_length(text:str) -> bool:
    return len(text) >= 8

def check_value_greater_than_100(number:int | float) -> bool:
    return number > 100

def checks_all_values_greater_than_100(number_list:list[int | float]) -> bool:
    return all([i > 100 for i in number_list])

def has_vowels(text:str) -> bool:
    return any([i in text for i in 'aeiou'])

def is_even(number:int) -> bool:
    return number % 2 == 0