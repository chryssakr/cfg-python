# input function

# Exercise 2.1: Write a program that asks two questions using input() then prints the values that were entered.
# You can choose any questions that you want.

# name = input("What is your name?") # always returns a string
# age = input("What is your age?")
# age_next_year = int(age) + 1
# print(f"Hello, my name is {name}, my age is {age}. Next year I'll be {age_next_year}.")
# print(f"{name=}, {age=}")

# Exercise 2.2: You have friends at your house for dinner and you've accidentally burnt the lasagne. Time to order pizza.
# Write a program calculate how many pizzas you need to feed you and your friends

# friends = input("How many friends are you feeding?")
# pizzas_per_friend = 0.5
# total_pizzas = int(friends) * pizzas_per_friend
# print(f"You need {total_pizzas} pizzas to feed your {friends} friends!")

# Python Modules
# import <name_of_module>
# from <name_of_module> import <specific_package_name>
# import math -> mathematical functions
# import datetime -> date and time value manipulation
# import timeit -> time the execution of small blocks of Python code
# import re -> regular expressions
# import copy -> duplicating objects
import datetime
"""
%a: Returns the first three characters of the weekday, e.g. Wed.
%A: Returns the full name of the weekday, e.g. Wednesday.
%b: Returns the first three characters of the month name.
%B: Returns the full name of the month, e.g. September.
%Y: Returns the year in four digit format
%Y: Returns the year in four-digit format.
%d: Returns day of the month, from 1 to 31.
%w: Returns the weekday as a number, from 0 to 6, with Sunday being 0.
%m: Returns the month as a number, from 01 to 12.
%p: Returns AM/PM for time.
%f: Returns microsecond from 000000 to 999999.
%Z: Returns the timezone.
%H: Returns the hour.
%M: Returns the minute, from 00 to 59.
%S: Returns the second, from 00 to 59.
"""

x = datetime.datetime.now()
# help(datetime.datetime.now())
print(x)

my_date = datetime.date(2020, 12, 31)

print(my_date.strftime("%d-%b-%Y"))

# For loops
for number in range(4):
    print(number)
print("-----")    

for char in "hello":
    print(char)
print("-----")    

for pet in ["Lola", "Babybel", "Cheddar"]:
    print(pet)

# While loops
# Due to social disctancing, only 10 people are allowed to be inside a shot at the same time.
# This program invites people in the queue to come in while we have some capacity.
store_capacity = 5

while store_capacity > 0:
    print(f"Please come in. We have {store_capacity} spaces available")
    store_capacity = store_capacity - 1
    
print("Store full. Please wait for someone to leave")

# Functions
def hello():
    print("Hello class!")
    
hello()
# I can put a default for language:
def hello_name(name, language = "Python"):
    print(f"Hello {name}, we're learning {language}!")
    
name = "Olya"
hello_name(name)
name = "Kate"
language = "French"
hello_name(language=language, name=name)

def sum(x, y):
    return (x + y)
    
result = sum(10, 5)
print(f"Our result is {result}")

# Exercise 2.6: Complete the function to return the area of a circle

def circle_area(radius):
    area = 3.14 * (radius ** 2)
    return area

circle_1 =  circle_area(10)

print(circle_1)

def times_two(num):
    result = num * 2
    return result
for number in range(3):
    multiplication = times_two(number)
    print(multiplication)
    