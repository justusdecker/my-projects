"""
(c) Masterschool
(c)2025 Justus Decker - coding solutions
"""

"""
🧬Mutability🧬

Guidelines
Work in PyCharm.
Test your code periodically in PythonTutor. 
Challenge 1 - ✏️ Lists
Create a list named original_list with at least 5 elements (e.g., numbers, strings, or a mix of both).

Print the original list.
Modify the first element of the list and print the list again.
Append a new element to the end of the list and print the list.
Use slicing to change a subset of the list (e.g., replace elements from index 2 to 4 with new values) and print the updated list.
"""

# example
original_list = [1,2,3,4,5]
print(original_list)
original_list[0] = 2
print(original_list)
original_list.append(3)
print(original_list)
original_list[:2] = 8,7
#start,stop,xxxx
print(original_list)

"""
Challenge 2 - 🔐 Strings
Create a string named original_string with at least 6 characters.

Print the original string.
Modify the third character of the string and print the string again.
Concatenate a new string to the original string and print the updated string.
Use string slicing to change a subset of the string (e.g., replace characters from index 1 to 4 with new characters) and print the updated string.
"""
# example
original_string = 'Hello World!'
print(original_string)
original_string = list(original_string)
original_string[2] = "r"
original_string = "".join(original_string)
print(original_string)
original_string += " Python is nice!"
print(original_string)
original_string = list(original_string)
original_string[:4] = "NOPE"
original_string = "".join(original_string)
print(original_string)

"""
Bonus Challenge - 🔐✏️ Combine Both!
Combine the concepts of lists and strings:

Create a list of strings where each element is a word.
b. Choose one of the words and modify it by changing some characters.
c. Print the updated list of strings.
"""

# example
my_strings = ['Merry', 'Frodo', 'Sam', 'Pippin']
print(my_strings)
temp = list(my_strings[0])
temp[1] = "a"
temp = "".join(temp)
my_strings[0] = temp
print(my_strings)