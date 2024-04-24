# the following messages are the same
# message = 'I need to buy {} nails'.format(total_nails)
# message = f'I need to buy {total_nails} nails'

# Question 1
# To fix it we need to change chairs so it's not a string but an integer
# I've also changed the name so it's more indicative
chairs = 15
nails_per_chair = 4
total_nails = chairs * nails_per_chair
message = f'I need to buy {total_nails} nails'
print(message)

# Question 2
# To fix it we need to put Penelope in quotes
# Otherwise it's as if we're referring to a variable named Penelope
my_name = "Penelope"
my_age = 29
message = f'My name is {my_name} and I am {my_age} years old'
print(message)

# Question 3
import math
eggs_per_box = 6
eggs_per_omelette = 4
boxes = 6
omelettes = eggs_per_box * boxes / eggs_per_omelette
omelettes = math.trunc(omelettes)
print(f'You can make {omelettes} omelettes with {boxes} boxes of eggs.')