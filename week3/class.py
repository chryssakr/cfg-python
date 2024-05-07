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

sides = int(input("How many sides on the die?: "))
random_int = random.randint(1, sides)
print(f"You rolled a {random_int}")