# variables are containers for values
# there are four basic datatypes a variable can hold:

# strings

# strings are variables consisting of only words/ letters

First_name = "Adrian"

Food = "tostones"

print(f"This user is named {First_name}")

print(f"{First_name} likes to eat {Food}")

# integers

# integers are variables made of exclusively whole numbers

age = 19
quantity = 40

print(f"{First_name} is {age} years old")
print(f"He has Bought {quantity} {Food} to eat")

# floats
# floats are variables made of decimal numbers

cost = 10.99
wallet = 894.63
total_spent = cost * quantity
print(f"each {Food} costs ${cost} to purchase")
print(f"Adrian had ${wallet} to spend")
print(f"If he used his ${wallet} to buy {quantity} {Food} for {cost} each, he spent {total_spent}")

# Boolean
# booleans are either true or false

isHungry = True

if isHungry:
    print("Adrian is very hungry")

else:
    print('Adrian is not very hungry')
