import random
import string
character=string.ascii_letters
number = string.digits
symbol =string.punctuation
print("welcome to pasword generator!")
n_letters=int(input("number of  letters you want in your password:\n "))
n_symbols=int(input("number of symbols you want in your password:\n "))
n_numbers=int(input("number of digits you want in your password:\n "))
password=""
for i in range (1,n_letters+1):
    char=(random.choice(character))
    password +=char
for i in range (1,n_symbols+1):
    char=(random.choice(symbol))
    password +=char
for i in range (1,n_numbers+1):
    char=(random.choice(number))
    password +=char
print(password)
print("successfully your password is generated!")
