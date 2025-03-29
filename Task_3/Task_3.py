# Problem 1
#  Create a dictionary representing a library catalogue. Each book should have a title, author, and publication year.

library_catalogue = {"Moby-Dick":"Herman Melville (1851)",
                     "War and Peace":"Leo Tolstoy (1869)",
                     "Crime and Punishment":"Fyodor Dostoevsky (1866)",
                     "Frankenstein":"Mary Shelley (1818)"}

for key,value in library_catalogue.items():
    print (f"{key}:{value}")


# ---------------------------------------------------------------------------------------------------------------------------
#  Problem 2
#  Generate a random password of 8 characters, including a mix of uppercase letters, lowercase letters, and numbers.

import random
import string

def generate_password(length=8):
    
    uppercase = string.ascii_uppercase  
    lowercase = string.ascii_lowercase  
    digits = string.digits              
    
    
    all_chars = uppercase + lowercase + digits
    
    # Ensure at least one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits)
    ]
    
    
    for _ in range(length - 3):
        password.append(random.choice(all_chars))
    
    
    random.shuffle(password)
    
    
    return ''.join(password)


password = generate_password()
print("Generated Password:", password)


# ---------------------------------------------------------------------------------------------------------------------------
#  Problem 3
#  Implement a guessing game where the computer generates a random number between 1 and 100, and the user has to guess the number.

import random

low = 1
high = 100
gusses = 0

num = random.randint(low , high)

while True:
    guss = int(input (f"Enter random num betwen ({low}-{high})"))
    gusses += 1

    if guss > num:
        print ("The guss is high")
    elif guss < num:
        print ("The guss is low")
    else:
        print ("You are correct !!")
        break
print (f"you took {gusses} of gusses ")



# ---------------------------------------------------------------------------------------------------------------------------
#  Problem 4
#  Write a function that takes two sets as input and returns a new setcontaining the common elements.

def get_common_elements():
    
    input1 = input("Enter first set (comma-separated): ")
    input2 = input("Enter second set (comma-separated): ")
    
    
    set1 = set(x.strip() for x in input1.split(','))
    set2 = set(x.strip() for x in input2.split(','))
    
    
    return set1 & set2


result = get_common_elements()
print("Common elements:", result) 


# ---------------------------------------------------------------------------------------------------------------------------
#  Problem 5

def is_leap(year):
    """Determine if a year is a leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Read input from STDIN (as specified in the problem)
year = int(input())
print(is_leap(year))  

# ---------------------------------------------------------------------------------------------------------------------------
#  Problem 6 (Bouns)
#  Write a program that asks the user for input and handles the possibility of theuser entering a non-numeric value

def get_number():
    while True:
        try:
            num = float(input("Enter a number: "))
            return num
        except ValueError:
            print("That's not a valid number. Please try again.")

print("Number Input Program")
user_number = get_number()
print(f"You entered: {user_number}")


