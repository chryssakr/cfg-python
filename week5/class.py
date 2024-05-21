# reading and writing from files
# with open("people.txt", "w+") as text_file:
#     people = "Kerry \nSusan \nSonja"
#     text_file.write(people)

# with open("people.txt", "a+") as text_file:
#     people = "\nSomething else"
#     text_file.write(people)
    
# with open("people.txt", "r") as text_file:
#     contents = text_file.read()
# print(contents)

""""**Exercise 5.1:** 

Create a to-do list program that writes user input to a file

The program should:
- Ask the user to input a new to-do item
- Add a new to do item to the existing to-do items
- Read the contents of the to-do items

You will need to manually create a new file called `todo.txt` in the same folder as your 
program before you start"""

# new_todo = input("Give a new todo list item: ")
# with open("todo.txt", "a+") as todo_file:
#     todo_file.write(new_todo)
    
# with open("todo.txt", "r") as todo_file:
#     contents = todo_file.read()
# print(contents)

# csv: comma separated values
# item1, item2, item3 etc
# tsv: tab separated values
# pip: a package manager
# import pandas as pd

# people_data = pandas.read_csv("people.txt")
# print(people_data)

# make_data = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]})
# print(make_data)
# make_data.to_csv("people_and_ages.csv", index = False)

# trees_data = pd.read.csv("data/trees.csv") 
# heights = []

# API: Application Programming Interface
import requests
from pprint import pprint # pretty print

pokemon_number = input("What is the pokemon number you want?")

url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'
response = requests.get(url)
print(response)

pokemon = response.json()
# print(pokemon)
# pprint(pokemon)
pprint(pokemon["name"])
"""
**Exercise 5.3:** Get the *height* and *weight* of a specific Pokemon and print the output

Extension: Print the names of all of a specific Pokemon's moves
"""

pprint(pokemon["height"])
pprint(pokemon["weight"])
moves = pokemon["moves"]
for move in moves:
    print(move["move"]["name"])