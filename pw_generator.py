from random import randint
import string
chars = string.ascii_letters + string.digits + string.punctuation

def generatePassword(length:int):
    password = ''
    for i in range(length):
        password += chars[randint(0,len(chars)-1)]
    return password

def generatePassword1(length:int):
    return ''.join([chars[randint(0,len(chars)-1)] for i in range(length)])

print(generatePassword1(16))