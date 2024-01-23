import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
x=int(input("How many letters would you like in your password ?\n"))
y=int(input("How many symbol would you like?\n"))
z=int(input("How many number would you like?\n"))
password=""
for char in range(1,x+1):
    password+=random.choice(letters)
for char in range(1,y+1):
    password+=random.choice(numbers)
for char in range(1,z+1):
    password+=random.choice(symbols)  
print(password)
l=list(password)
random.shuffle(l)
l=''.join(l)
print(f"Here is your password:{l}")