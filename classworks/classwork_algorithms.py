
#1️⃣ Lowest Common Divisor / kgV
    
def lcd(a,b):
    c,d = a,b
    while c: c,d = d % c,c
    return int(float(a * b) / d)

print(lcd(12,18))
#2️⃣ Create an algorithm that checks if an integer is a palindrome.
def palindrome(number:int):
    return str(number) == str(number)[::-1]
print(palindrome(12321))

#3️⃣String Permutations
def permutation(a:str,b:str):
    return {k: a.count(k) for k in a} == {k: b.count(k) for k in b}
print(permutation("ENKEL","NELKE"))