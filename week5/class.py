# reading and writing from files
# with open("data/people.txt", "w+") as f:
#     people = "Kerry \nSusan \nSonja"
#     f.write(people)

# with open("data/people.txt", "a+") as f:
#     people = "\nSomething else"
#     f.write(people)
    
# with open("data/people.txt", "r") as f:
#     contents = f.read()
#     print(contents)

""""**Exercise 5.1:** 

Create a to-do list program that writes user input to a file

The program should:
- Ask the user to input a new to-do item
- Add a new to do item to the existing to-do items
- Read the contents of the to-do items

You will need to manually create a new file called `todo.txt` in the same folder as your 
program before you start"""

# new_item = input("Give a new todo list item: ")
# with open("data/todo.txt", "a+") as f:
#     f.write("\n" + new_item)
    
# with open("data/todo.txt", "r") as f:
#     contents = f.read()
# print(contents)

# csv: comma separated values
# item1, item2, item3 etc
# tsv: tab separated values
# pip: a package manager
import pandas as pd

# # creating a dataframe with columns Name and Age and 4 rows of data
# people_data = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie", "Joe"],
#                           "Age": [25, 30, 35, 32]})

# # pd.read_csv() function in the pandas library
# # is used to read a CSV file into a DataFrame
# people_data = pd.read_csv("data/people_and_ages.csv")
# print(people_data)

# # .to_csv: creating a csv, index = False will give me
# # the data w/o the first column with the row numbers in it
# # sep = "\t" will set the delimiter to a tab. Default is ',' for comma.
# trees_data = pd.read_csv("data/trees.csv")
# trees_data.to_csv("data/trees.csv", index = False)

# # I can also read the data with a different delimiter
# trees_with_tabs = pd.read_csv("data/trees.csv", sep = "\t")

# API: Application Programming Interface
# allows access to data
import requests
from pprint import pprint # pretty print

pokemon_number = input("What is the pokemon number you want?: ")

url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'
# request data from the API
response = requests.get(url)
# print(response) # response 200: everything ok, 400 or 404: errors

# turn the data into a json object (it's like a dictionary)
pokemon = response.json()
# print(pokemon)
# pprint(pokemon)
# pprint(pokemon["name"])
"""
**Exercise 5.3:** Get the *height* and *weight* of a specific Pokemon
and print the output
Extension: Print the names of all of a specific Pokemon's moves
"""

height = pokemon["height"]
weight = pokemon["weight"]
moves = pokemon["moves"]
print(f"{height=}, {weight=}")
for move in moves:
    print(move["move"]["name"])
