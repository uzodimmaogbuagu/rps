import random
#Welcome banner
print("Welcome to RPS Championship")
# initilize player and computer score
player_score = 0
computer_score = 0

while True:
    user_option = input(
        "Choose your option between \n"
        "1. Rock\n"
        "2. Paper\n"
        "3. Scissors\n"
    )

    user_input = int(user_option)

    if user_input >= 1 and user_input <= 3:
        break

    print("Invalid! Choose between 1 and 3")


choices_list = ["Rock", "Paper", "Scissors"]

computer_choice = random.choice(choices_list)
user_choice = choices_list[user_input - 1]

print(f"You chose {user_choice}")
print(f"Computer chose {computer_choice}")


# Determine the winner

if user_choice == computer_choice:
    print("It's a draw!")

elif (
    (user_choice == "Rock" and computer_choice == "Scissors")
    or
    (user_choice == "Paper" and computer_choice == "Rock")
    or
    (user_choice == "Scissors" and computer_choice == "Paper")
):
    print("You win!")
    player_score += 1

else:
    print("Computer wins!")
    computer_score += 1

# Display the scores

print("Player score:", player_score)
print("Computer score:", computer_score)


