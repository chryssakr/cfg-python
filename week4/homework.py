"""
Question 1
I have a list of things I need to buy from my supermarket of choice.
I want to know what the first thing I need to buy is.
However, when I run the program it shows me a
different answer to what I was expecting?
"""
shopping_list = [
    "oranges",
    "cat food",
    "sponge cake",
    "long-grain rice",
    "cheese board"
]

print(shopping_list[0]) # change the index to 0

"""
Question 2
I'm setting up my own market stall to sell chocolates. 
I need a basic till to check the prices of different chocolates that I sell.
I've started the program and included the chocolates and their prices.
Finish the program by asking the user to input an item and then output its price.
"""
chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00
}

new_chocolate_type = input("Give a new chocolate type: ")
new_chocolate_price = float(input("How much does it cost? "))
chocolates[new_chocolate_type] = new_chocolate_price
print(chocolates)

chocolate_to_buy = input("Which chocolate would you like to buy? white/milk/dark/vegan ").lower()
print(f"Your {chocolate_to_buy} chocolate costs £{chocolates[chocolate_to_buy]}")

"""
Write a program that simulates a lottery. The program should have a list of seven numbers that
represent a lottery ticket. It should then generate seven random numbers. After comparing the two
sets of numbers, the program should output a prize based on the number of matches:
● £20 for three matching numbers
● £40 for four matching numbers
● £100 for five matching numbers
● £10000 for six matching numbers
● £1000000 for seven matching numbers
"""

import random
winning_ticket = [1, 4, 8, 15, 16, 23, 42]
def get_user_numbers():
    """gets and validates user's lottery numbers"""
    user_numbers = []
    for i in range(1, 8):
        while True:
            number = int(input(f"Enter your lottery number {i}: "))
            if 1 <= number <= 49 and number not in user_numbers:
                user_numbers.append(number)
                break
            elif number in user_numbers:
                print("Duplicate number. Please try again")
            else:
                print("Invalid number. Please try again")
    return user_numbers

def get_lottery_numbers(seed = None):
    """Generates 7 random unique lottery numbers"""
    if seed is not None:
        random.seed(seed)
        lottery_numbers
    return lottery_numbers

def count_matches(user_numbers, lottery numbers)

matches = 0
for i in range(7):
    if winning_ticket[i] in ticket:
        matches += 1
winning_amounts = {
    3: 20,
    4: 40,
    5: 100,
    6: 10000,
    7: 1000000
}
if matches > 2:
    print(f"You had {matches} matches. You won £{winning_amounts[matches]}.")
else:
    print(f"You had {matches} matches. You didn't win anything, try again.")

def main():
    user_numbers = get_user_numbers()
    lottery_numbers = get_lottery_numbers()
    match_count = count_matches(user_numbers, lottery_numbers)
    print(f"The lottery numbers are: {lottery_numbers}")
    if prize > 0:
        print("Congratulations! You have won £{prize} with {match_count} matching numbers!")

if __name__ == "__main__":
    main()