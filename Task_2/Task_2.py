# Problem 1
# takes any numbers from user terminates if user enters -1   then prints largest and smallest number

numbers = []

while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    numbers.append(num)

if numbers:
    print(f"Largest number: {max(numbers)}")
    print(f"Smallest number: {min(numbers)}")
else:
    print("No numbers were entered.")


# -------------------------------------------------------------------------------------------
# Problem 2
# takes today’s date and print tomorrow’s date

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

if month == 12 and day == 30:  # New Year's Eve
    day, month, year = 1, 1, year + 1
elif day == 30 and month < 12 :
    day , month = 1, month +1
else:
    day += 1

print(f"Tomorrow: Day: {day} Month: {month} Year: {year}")


# -------------------------------------------------------------------------------------------
# Problem 3
# takes a positive integer as input and calculates its factorial.

import math
num = int(input("Enter a positive num: "))
if num<0:
    print ("Please Enter positive num")
else:
    result = math.factorial(num)
    print (f"thr factorial of input num is: {result}")


# -------------------------------------------------------------------------------------------
# Problem 4
#  takes a sentence as input and reverses the order of words in the sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_sentence = ' '.join(reversed(words))
print(reversed_sentence)


# -------------------------------------------------------------------------------------------
# Problem 5
# checks if a given word is a palindrome.A palindrome is a word that reads the same backward as forward.

word = input("Enter a word: ")

if word == word[::-1]:
    print(f"The word '{word}' is a palindrome.")
else:
    print(f"The word '{word}' is not a palindrome.")


# -------------------------------------------------------------------------------------------
# Problem 6
#  takes a positive integer as input and calculates the sum of all even numbers from 1 to that integer..

n = int(input("Enter a positive integer: "))
sum_even = 0

for num in range(1, n + 1):
    if num % 2 == 0:  
        sum_even += num    

print(f"The sum of even numbers from 1 to {n} is {sum_even}")



# -------------------------------------------------------------------------------------------
# Problem 7
# takes a positive integer as input and finds its prime factors.

n = int(input("Enter a positive integer: "))
factors = []
d = 2

while n > 1:
    while n % d == 0:
        factors.append(d)
        n = n // d
    d += 1

print("Prime factors:", factors)

