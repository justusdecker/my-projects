"""
(c) Masterschool
(c) 2025 Solution & refactoring by Justus Decker
1️⃣ Odd
The following program is supposed to check if a number is odd, but it's buggy
notion image
Try to debug and fix the bug.

2️⃣ Email Address Generator
This program converts a username to an email address, but it's buggy. Catch and fix the bug(s).

3️⃣Compute Area
This program is supposed to calculate the area of a rectangle, but it is buggy. Catch and fix the bugs.
"""

"""
def is_odd_number(num):

  if num % 2 = 0:
    return True 
  else:
    return False 

def main():
	print(is_odd_number(4)) # Expected False
	print(is_odd_number(7)) # Expected True

if __name__ == "__main__":
	main()
"""

def is_odd_number(num):

  return bool(num % 2)

def main():
	print(is_odd_number(4)) # Expected False
	print(is_odd_number(7)) # Expected True

if __name__ == "__main__":
	main()
 
"""
def remove_special_char(username):
    updated_username = ""
    for char in username:
        if char in ";.@#$%ˆ&*:_ ":
            updated_username += char
    return updated_username

def add_at_symbol(username):
    return username + "@"

def add_domain_name(username):
    return "mail" + username + ".com"

def main():
    username = "user&#123_ @" # username we want to convert to email
    new_username = remove_special_char(username)
    new_username_with_at = add_at_symbol(new_username)
    user_email = add_domain_name(new_username_with_at)
    print(user_email) # Expected user123@mail.com

if __name__ == "__main__":
    main()
"""
class Email:
    def get(username:str):
        """Get User E-Mail"""
        user_email = Email.concat(Email.remove_special_chars(username))
        return user_email
    def remove_special_chars(username):
        """ Remove special characters and space from the username """
        return "".join(char for char in username if char not in  ";.@#$%ˆ&*:_ ")
    def concat(loc,glb:str="mail",tld:str="net"):
        """combine: local part + global part + seperator + top level domain""" 
        return f"{loc}@{glb}.{tld}"

if __name__ == "__main__":
    print(Email.get("user&#123_ @"))

"""
def compute_area(length, width):

    return length + width

def get_dimensions():
    length = input("Enter the length of the rectangle: ")
    width = input("Enter the width of the rectangle: ")
    return width, length 

def main():
    length, width = get_dimensions()
    area = compute_area(length, width)
    print(f"The area of the rectangle is: {area}")

if __name__ == "__main__":
    main()
"""

def compute_area():
    """Get user input & Compute the area of a rectangle"""
    return int(input("Enter the width of the rectangle in meter: ")) * int(input("Enter the length of the rectangle in meter: "))

def main():
    print(f"The area of the rectangle is: {compute_area()}qm")

if __name__ == "__main__":
    main()

