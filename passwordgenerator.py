import random
import string
characters=string.ascii_letters+string.digits+string.punctuation
length=int(input("Enter the length of Password:"))
password =" "
for i in range(length):
    password= password+ random.choice(characters)
print(password)