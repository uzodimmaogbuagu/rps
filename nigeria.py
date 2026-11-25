# import random    

# player_state = 0
# while player_state < 1 or player_state > 3:
#     player_input = input(
#         "Enter option: \n"
#         "1 for rock\n"
#         "2 for scissors\n"
#         "3 for paper\n"
#         "Your choice: "
#     )
#     player_choice = int(player_input)
    
#     if player_choice < 1 or player_choice > 3:
#         print("Invalid choice, choose again.\n")
#     else:
#         player_state = player_choice
        
# options = [1, 2, 3]
# computerchoice = random.choice(options)

# # Added an 'f' before the string so the actual number shows up
# print(f"computer choose: {computerchoice}")

# # Complete game logic (including winning, losing, and ties)
# if player_choice == computerchoice:
#     print("It's a tie!")
# elif (player_choice == 1 and computerchoice == 2):
#     print("you win")
# elif (player_choice == 2 and computerchoice == 3):
#     print("you win")
# elif (player_choice == 3 and computerchoice == 1):
#     print("you win")
# else:
#     print("computer win")


def myfunc():
    x = 300
    print(x)
    
myfunc()