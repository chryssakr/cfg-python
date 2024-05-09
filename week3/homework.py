# Question 1
# Create a program that tells you whether or not you need an umbrella when you leave the house.
# The program should:
# 1. Ask you if it is raining using input()
# 2. If the input is 'y', it should output 'Take an umbrella'
# 3. If the input is 'n', it should output 'You don't need an umbrella'

is_raining = input("Is it raining outside? y/n")
if is_raining == "y":
    print("Take an umbrella")
else:
    print("You don't need an umbrella")
    
# Question 2
# I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit.
# I've written a program to check that I can afford the cost, but something doesn't seem right.
# Have a look at my program and work out what I've done wrong

my_money = int(input('How much money do you have? ')) # it needs to be casted into int
boat_cost = 20 + 5 # it needs an underscore
if my_money < boat_cost:
    print('You cannot afford the boat hire') # it wasn't indented and the logic is the other way around
else:
    print('You can afford the board hire') # it wasn't indented
    
# Question 3
# Your friend works for an antique book shop that sells books between 1800 and 1950 and wants to
# quickly categorise books by the century and decade that they were written.
# Write a program that takes a year (e.g. 1872) and outputs the century and decade
# (e.g. "Nineteenth Century, Seventies")

publication_year = input("What's the publication year of the book?")
cent = int(publication_year[1])
dec = int(publication_year[2])
if cent == 8:
    century = "Eighteenth"
elif cent == 9:
    century = "Nineteenth"
if dec == 1:
    decade = "Tens"
elif dec == 2:
    decade = "Twenties"
elif dec == 3:
    decade = "Thirties"
elif dec == 4:
    decade = "Forties"
elif dec == 5:
    decade = "Fifties"
elif dec == 6:
    decade = "Sixties"
elif dec == 7:
    decade = "Seventies"
elif dec == 8:
    decade = "Eighties"
elif dec == 9:
    decade = "Nineties"
print(f"{century} Century, {decade}")