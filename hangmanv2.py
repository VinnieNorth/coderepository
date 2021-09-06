import random

number = (random.randint(0,100))

print(number)

guess = (int(input("Please enter a guess for the number")))
count = 0
while guess != number:
    if guess <= number:
        print("Your number is too small, please try again")
        count = count + 1
        guess = (int(input("Please enter a guess for the number")))

    elif guess >= number:
        print("Your number is too big, please try again")
        count = count + 1
        guess = (int(input("Please enter a guess for the number")))

newcount = str(count)
print("Congrats u won")

print("you guessed "+newcount+" times")