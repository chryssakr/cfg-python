# carrots = int(input('How many carrots do you have? '))
# rabbits = 6
# if rabbits > carrots:
#     print('There are not enough carrots')
# elif rabbits < carrots:
#     print('There are too many carrots')
# else:
#     print('You have the right number of carrots')
    
# # Lists
# # List: an ordered collection of values
# # intergers
# lottery_numers = [4, 8, 15, 20]
# # strings
# student_names = ["Diedre", "Kerry", "Jo"]
# # can be a mix of data types
# person = ["Jess", 32]

# print(student_names[2]) # it will print "Jo"
# student_names[0] = "Jane"
# print(student_names) # Now the first name will be Jane instead of Diedre

# Exercise 4.1: When I'm travelling in the winter I often forget to pack warm clothes.
# Let's write a program to help me to remember the right clothes.
# The program should check if the first item in the clothes list is "shorts".
# If it is it should change the value to "warm coat".

# clothes = [
#     "shorts",
#     "shoes",
#     "t-shirt",
# ]
# if clothes[0] == "shorts":
#     clothes[0] = "warm coat"
# print(clothes)

# List functions
# len() - number of items
# max() - max value in list
# min() - min value in list
# sorted() - sorts
# reversed() - reverses (does not sort)

# costs = [1.2, 2.5, 0.5, 4.75, 3.25]

# print(len(costs))
# print(max(costs))
# print(min(costs))
# print(sorted(costs))
# print(list(reversed(costs)))

"""
Exercise 4.2: Make a list of game scores. Using list functions write code to output
information of the scores in the following format:
Number of scores: 10
Highest score: 200
Lowest score: 3
Extension: Output all of the scores in descending order
"""

# game_score = [30, 200, 45, 3, 60, 24, 26, 56, 78, 98]
# print(f"Number of scores: {len(game_score)}")
# print(f"Highest score: {max(game_score)}")
# print(f"Lowest score: {min(game_score)}")
# print(f"Scores in descending order: {list(reversed(sorted(game_score)))}")

# append() and in
# in - check if value is in the list - returns True/False

# student_names = ["Diedre", "Kerry", "Jo"]
# student_name_query = input("Which student are you looking for?")
# if student_name_query in student_names:
#     print(f"{student_name_query} is in the class")
# else:
#     print(f"{student_name_query} is not in the class")

# append() - add to the list
# student_names.append("Jane")
# print(student_names)

"""
Exercise 4.3: Whenever I'm shopping and I buy some bread I always forget to buy butter.
Create a list and if 'bread' is in the list, add 'butter' to the shopping list.
Try running the program with and without bread in the list to check that your program works.
Remember the in operator checks if an item is in a list and the .append() method adds an item to a list.
"""
# shopping_list = [
#     "bread",
#     "cheese",
#     "pop tarts",
#     "carrots"
# ]
# if "bread" in shopping_list:
#     shopping_list.append("butter")
# if "bread" not in shopping_list:
#     shopping_list.append("bread")
#     shopping_list.append("butter")
    
# using loops and lists together

# student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
# count = 0
# for student_name in student_names:
#     count += 1
#     print(student_name)
# print(f"There are {count} students.")

"""
Exercise 4.4: I want to work out how much money I've spent on lunch this week.
I've created a list of what I spent each day.
Write a program that uses a for loop to calculate the total cost
"""
# costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
# total_cost = 0.0
# for cost in costs:
#     total_cost += cost
# total_cost = round(total_cost, 2)
# # total_cost = sum(costs)
# print(f"You spent £{total_cost} on lunches this week.")

# Dictionaries - store a collection of labelled items
# each item has a key and value in the format {key: value}

# person = {
#     "name": "Jessica",
#     "age": 23,
#     "height": 172
# }
# print(person["height"])

"""
Exercise 4.5: Print the values of name, post_code and street_number from the dictionary
Extra: Print out longitute and latitude
"""
# place = {
#     "name": "The Anchor",
#     "post_code": "E14 6HY",
#     "street_number": "54",
#     "location": {
#         "longitude": 127,
#         "latitude": 63,
#     }
# }
# print(f"Name: {place["name"]}, Postcode: {place["post_code"]}, Street Number: {place["street_number"]}")
# print(f"Longitude: {place["location"]["longitude"]}, Latitude: {place["location"]["latitude"]}")

# putting dictionaries inside a list is very common
# people = [{"name": "Jessica",
#            "age": 23},
#           {"name": "Trisha",
#            "age": 24}]
# for person in people:
#     print(f"Name: {person["name"]}, Age: {person["age"]}")
    
"""
Exercise 4.6: Using a for loop, output the values name,
colour and price of each dictionary in the list
"""
# fruits = [
#     {'name': 'apple', 'colour': 'red', 'price': 0.12},
#     {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
#     {'name': 'pear', 'colour': 'green', 'price': 0.19}
# ]
# for fruit in fruits:
#     print(f"Name: {fruit["name"]}, Colour: {fruit["colour"]}, Price: {fruit["price"]}")

# Random choice
# choice() - random module, returns random choice from list
# import random
# colours = ["red", "green", "yellow"]
# chosen_colour = random.choice(colours)
# print(chosen_colour)

"""
Exercise 4.7: Write a program to create a random name. 
You should have a list of random first-names and a list of last-names. 
Choose a random item from each and display the result.
Extension: Using list of verbs and a list of nouns, create randomised sentences
"""
import random
# first_names = ["Dierdre", "Patricia", "Edelbert"]
# last_names = ["Johnson", "Davis", "Oak"]
# random_first = random.choice(first_names)
# random_last = random.choice(last_names)
# print(f"My random name: {random_first} {random_last}")

# names = ["Zipi", "Ishay", "Maya", "Ethan", "Not_Mummy"]
# tasks = ["toilet cleaner", "bed maker", "dishwasher loader", "floor scrubber"]
# random_name = random.choice(names)
# random_task = random.choice(tasks)
# print(f"{random_name} is a {random_task}")

# first_name = ["Sally", "Catherine", "Trisha", "Heather", "Jane"]
# last_name = ["Doe", "Brooks", "O'Connor", "Luo", "Chu"]
# verbs = ["reads", "jumps", "runs", "leaps", "writes"]
# nouns = ["a book", "her home", "the wall", "on water", "the tree"]
# print(f"{random.choice(first_name)} {random.choice(last_name)} {random.choice(verbs)} {random.choice(nouns)}")

trees = [
    {'leaf_colour': 'green', 'height': 2120},
    {'leaf_colour': 'green', 'height': 2300},
]
new_tree = {
    'leaf_colour': 'green',
    'height': 1020
}
trees.append(new_tree)
print(trees)