import random

adjectives = ["Fierce", "Timid", "Loyal", "Funny", "Shy", "Courageous"]
animals = ["Giraffe", "Dog", "Panda", "Tiger", "Horse", "Snake"]

adjective = random.choice(adjectives)
animal = random.choice(animals)
lucky_number = random.randint(1, 99)

print("What is your name?")
name = input("")

print(f"{name}, your codename is: {adjective} {animal}")
print(f"Your lucky number is: {lucky_number}")

