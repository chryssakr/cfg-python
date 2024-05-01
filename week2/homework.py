# Question 1
# Explain what this program does
# It prints 0-99 times the letter o
for number in range(100):
    output = 'o' * number
    print(output)
    
# Question 2
# Your boss really likes calculating VAT on their purchases. It is their favourite hobby. 
# They've written this code to calculate VAT and need your help to fix it.
def with_vat(amount):
    amount = amount * 1.2
    return amount
without_vat = 100
print(with_vat(without_vat))