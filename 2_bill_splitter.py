# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

bill = int(input('What is bill number? '))
persons = int(input('How many people here? '))
tip = int(input('What is your tip percent? '))
print('Each person should pay ' + str(bill/persons * (tip / 100 + 1)))
