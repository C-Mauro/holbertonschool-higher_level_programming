#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 
str1 = "Last digit of"
str2 = "is"

if number > 0 and last_digit > 5:
    print(f"{str1} {number} {str2} {last_digit} and is greater than 5")

if last_digit == 0:
    print(f"{str1} {number} {str2} {last_digit} and is 0")

if number < 0 and last_digit != 0:
    last_digit = -10 + last_digit
    print(f"{str1} {number} {str2} {last_digit} and is less than 6 and not 0")

elif number > 0 and last_digit < 6 and last_digit != 0:
    print(f"{str1} {number} {str2} {last_digit} and is less than 6 and not 0")
