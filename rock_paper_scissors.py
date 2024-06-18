import random

computer_win = 0
user_win = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor and Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    #rock:0 paper:1 scissor:2

    computer_choice = options[random_number]
    print("Computer picked", computer_choice+".")

    if user_input == "rock" and computer_choice == "scissor":
        print("You won!")
        user_win += 1
        continue

    elif user_input == "scissor" and computer_choice == "paper":
        print("You won!")
        user_win += 1
        continue
    elif user_input == "paper" and computer_choice == "rock":
        print("You won!")
        user_win += 1
        continue

    else:
        print("You lost!")
        computer_win += 1

print("You won", user_win, "times.")
print("Computer won", computer_win, "times.")
print("Goodbye!")
