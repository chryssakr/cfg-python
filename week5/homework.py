"""
Question 1
You're having coffee/tea/beverage of your choice with a friend that is
learning to program in Python. They're curious about why they would use pip.
Explain what pip is and one benefit of using pip.
"""
"""
Answer:
pip stands for "Pip Installs Packages." It's a package management system
used to install and manage software packages written in Python.
It's similar to npm in JS
"""

"""
Question 2
This program should save my data to a file, but it doesn't work when I run it.
What is the problem and how do I fix it?
"""
poem = 'I like Python and I am not very good at poems'
with open('data/poem.txt', 'w+') as poem_file:
    poem_file.write(poem)
    
"""
Question 3
In this session you used the Pokemon API to retrieve a single Pokemon.
I want a program that can retrieve multiple Pokemon and save their names
and moves to a file. Use a list to store about 6 Pokemon IDs.
Then in a for loop call the API to retrieve the data for each Pokemon.
Save their names and moves into a file called 'pokemon.txt'
"""
import requests
from pprint import pprint # pretty print

pokemon_amount = 6
pokemon_ids = []
while len(pokemon_ids) < pokemon_amount:
    pokemon_number = int(input("What is the pokemon number you want?: "))
    if pokemon_number not in pokemon_ids:
        pokemon_ids.append(pokemon_number)

# pokemon_number = input("What is the pokemon number you want?: ")

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
