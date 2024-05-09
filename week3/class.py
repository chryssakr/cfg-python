# for i in range(9):
#     print("~" * i)

# today = input("What day is it?: ")
# is_tuesday = today == "Tuesday"
# print(f"Today is Tuesday: {is_tuesday}")

# temp = float(input("What is the temp?: "))
# is_freezing = temp <= 0.0
# print(f"The temp is freezing: {is_freezing}")

# Exercise 3.1: You have a budget of £10 and want to write a program
# to decide which burger restaurant to go to.
# 1. Input the price of a burger using input()
# 2. Check whether the price is less than or equal (<=) 10.00
# 3. Print the result in the format below
# Burger is within budget: True
# Hint: remember to convert the input from a string to a decimal with float()

# burger_budget = 10.00
# burger_price = float(input("What's the price of the burger?"))
# is_within_budget = burger_price <= burger_budget
# print(f"Burger is within budget: {is_within_budget}")

# mars_choice = input("Would you like to go to Mars? y/n")
# is_willing = mars_choice == "y"
# affordable = input("Can you afford to visit Mars? y/n")
# is_affordable = affordable == "y"
# should_visit_mars = is_willing and is_affordable
# print(f"You can go to Mars: {should_visit_mars}")

# Exercise 3.2: Add code to your burger program to input whether 
# the restaurant has a vegetarian option. The output should say 
# whether the cost is within budget AND has a vegetarian option
# Restaurant meets criteria: True

# burger_budget = 10.00
# burger_price = float(input("What's the price of the burger?"))
# is_within_budget = burger_price <= burger_budget
# vegetarian_options = input("Is there a vegetarian option? y/n")
# is_vegetarian_friendly = vegetarian_options == "y"
# meets_criteria = is_within_budget and is_vegetarian_friendly
# print(f"Restaurant meets criteria: {meets_criteria}")

# password = input("password: ")
# if password == "codefirstgirls":
#     print("Success!")
    
# name = input("What is your name?: ")
# is_admin = name == "admin"
# password = input("password: ")
# is_password_correct = password == "dinosaur"
# if is_admin and is_password_correct:
#     print("Welcome!")
# if not is_admin or not is_password_correct:
#     print("Go away!")

# Exercise 3.3: Rewrite the output of your burger program to use if statements
# If it is a good choice it should be:
# This restaurant is a great choice!
# If it is not a good choice it should be:
# Probably not a good idea

# burger_budget = 10.00
# burger_price = float(input("What's the price of the burger?"))
# vegetarian_options = input("Is there a vegetarian option? y/n")
# is_within_budget = burger_price <= burger_budget
# is_vegetarian_friendly = vegetarian_options == "y"

# if is_within_budget and is_vegetarian_friendly:
#     print("This restaurant is a great choice!")
# if not is_within_budget or not is_vegetarian_friendly:
#     print("Probably not a good idea")

# password = input("password: ")
# if password == "codefirstgirls":
#     print("Success!")
# else:
#     print("Failure")

# name = input("What is your name?: ")
# is_admin = name == "admin"
# password = input("password: ")
# is_password_correct = password == "dinosaur"
# if is_admin and is_password_correct:
#     print("Welcome!")
# else:
#     print("Go away!")

# Exercise 3.4: Now that you've nished your burger, you want to pay for your food.
# Let's write a program to calculate your meal and apply a discount if applicable.
# If your total meal costs more than £20 and you have a discount,
# the price will be reduced by 10%. The program should print "Discount applied"
# or "No discount" depending on whether the discount criteria was met.

# meal_price = float(input("How much did your meal cost?"))
# discount = 0.1
# minimum_for_discount = 20

# if meal_price >= minimum_for_discount:
#     final_cost = meal_price - discount * meal_price
#     print(f"Discount applied! Amount to be paid: £{final_cost}")
# else:
#     print(f"No discount. Amount to be paid: £{meal_price}")

# dog_size = int(input("How big is the dog?: "))
# if dog_size > 75:
#     print("That is a BIG dog!")
# elif dog_size < 25:
#     print("That is a small dog!")
# else:
#     print("That is an average dog.")
    
# Exercise 3.5: You're cooking a pizza and need to check that the oven is at the right temperature.
# Write a program to:
# Ask the user to input the temperature
# Prints "The oven is too hot" if the temperature is over 200
# Prints "The oven is too cold" if the temperature is under 150
# Prints "The oven is at the perfect temperature" if the temperature is 180
# Prints "The temperature is close enough" for any other temperature

# temp = int(input("What's the temperature of the oven?: "))
# if temp > 200:
#     print("The oven is too hot")
# elif temp == 180:
#     print("The oven is at the perfect temperature")
# elif temp < 150:
#     print("The oven is too cold")
# else:
#     print("The temperature is close enough")

import random

# random_int = random.randint(1, 100)
# print(random_int)

# sides = int(input("How many sides on the die?: "))
# random_int = random.randint(1, sides)
# print(f"You rolled a {random_int}")

# Exercise 3.6: This program uses random to simulate a coin flip.
# To finish the program you will need to add the following:
# - If the random coin flip matches the choice input by the user then they win
# - Otherwise if the random coin flip does not match the choice input by the user then they lose

# def flip_coin():
#     random_number = random.randint(1, 2)
#     if random_number == 1:
#         side = "h"
#     else:
#         side = "t"
#     return side
# user_choice = input("Heads or Tails? h/t")
# computer_choice = flip_coin()
# result = user_choice == computer_choice
# print(f"Result of the flip: {result} {user_choice=} {computer_choice=}")

# Exercise 3.7: This program simulates rock, paper, scissors.
# The first winning condition has been added. 
# To finish the program you'll need to add all of the other winning and losing conditions.

# def random_choice():
#     choice_number = random.randint(1, 3)
#     if choice_number == 1:
#         choice = "r"
#     elif choice_number == 2:
#         choice = "p"
#     else:
#         choice = "s"
#     return choice
# user_choice = input("rock, paper or scissors? r/p/s")
# computer_choice = random_choice()
# result = user_choice == computer_choice
# print(f"Result of the flip: {result} {user_choice=} {computer_choice=}")

# Exercise 3.8: Not Quite Roulette
# Ask the user to enter the following three things using `input()`:
# - The amount they want to bet
# - A colour (red or black)
# - A number between 1 and 100
# 
# After generating a random number and colour:
# - If the colour matches, the users keeps the amount that was bet
# - If the number matches, the users wins double the amount that was bet
# - If the colour and number matches, the users wins 100 times the amount that was bet
# - When neither the colour or number matches the user wins 0
# - Output the amount the user won

# def colour():
#     random_number = random.randint(1, 2)
#     if random_number == 1:
#         colour = 'red'
#     else:
#         colour = 'black'
#     return colour
# user_bet = int(input("How much money do you want to bet?"))
# user_colour = input("Pick a colour, red or black: red/black")
# user_number = int(input("Pick a number from 1 to 100"))
# random_number = random.randint(1, 100)
# random_colour = colour()

# if user_colour == random_colour and user_number == random_number:
#     amount_won = 100 * user_bet
# elif user_colour == random_colour:
#     amount_won = user_bet
# elif user_number == random_number:
#     amount_won = 2 * user_bet
# else:
#     amount_won = 0
# print(f"You have won £{amount_won}")