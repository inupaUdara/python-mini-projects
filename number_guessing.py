import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter larger than 1 number")
        quit()
else:
    print("Please enter number")
    quit()

random_number = random.randint(1,top_of_range)

guess = 0

while True:
    guess += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter a number")
        continue

    if(user_guess == random_number):
        print("You got right")
        break
    else:
        print("You got wrong")
        

print("You got it in", guess, "guesses")




