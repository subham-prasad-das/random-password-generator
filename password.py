import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

plength = int(input("Enter the password length you would like to generate: "))
print("\n")

s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

random.shuffle(s)

print("Your generated password is: ")
print("".join(s[0:plength]))