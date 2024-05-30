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
# poem = 'I like Python and I am not very good at poems'
# with open('data/poem.txt', 'w+') as poem_file:
#     poem_file.write(poem)
    
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
from typing import Any
import csv

# Get the necessary pokemon ids from the user
def collect_pokemon_ids(no_of_pokemons: int = 6) -> set[int]:
    # initialise pokemon_ids as a set
    pokemon_ids: set[int] = set()
    pokemons_in_api = 248
    print(f"There are {pokemons_in_api} different pokemons to choose from!")
    while len(pokemon_ids) < no_of_pokemons:
        pokemon_number = int(input(f"Enter number for pokemon no{len(pokemon_ids) + 1}: "))
        if pokemon_number < 1 or pokemon_number > 248:
            print(f"The number you gave is out of bounds, please give a number from 1 to {pokemons_in_api}")
        elif pokemon_number not in pokemon_ids:
            pokemon_ids.add(pokemon_number)
        else:
            print("Duplicate entry detected. Give another number.")
    return pokemon_ids

# Get names and moves for the pokemons
def fetch_names_moves(pokemon_ids: set[int]) -> dict[int, dict[str, Any]]:
    pokemon_dict: dict[int, dict[str, Any]] = {}
    for pokemon_id in pokemon_ids:
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
        response = requests.get(url)
        pokemon = response.json()
        pokemon_data_dict = dict([("name", pokemon["name"]), ("moves", pokemon["moves"])])
        pokemon_dict[pokemon_id] = pokemon_data_dict
    return pokemon_dict

# Write the data from the pokemon dictionary to a file in csv format
def write_to_csv(pokemon_ids:set[int] ,pokemon_dict: dict[int, dict[str, Any]]) -> None:
    with open("data/pokemon.csv", "w+", newline = "") as f:
        field_names = ["id", "name", "moves"]
        writer = csv.DictWriter(f, fieldnames = field_names)
        writer.writeheader()
        for pokemon_id in pokemon_ids:
            writer.writerow({
                "id": pokemon_id,
                "name": pokemon_dict[pokemon_id]['name'],
                "moves": pokemon_dict[pokemon_id]['moves']
            })

def main() -> None:
    pokemon_amount = 6
    pokemon_ids = collect_pokemon_ids(pokemon_amount)
    pokemon_names_moves = fetch_names_moves(pokemon_ids)
    write_to_csv(pokemon_ids, pokemon_names_moves)
    
if __name__ == "__main__":
    main()
