# Rock, Paper, Scissors menu

# rock = 1
# paper = 2
# scissors = 3

# print("Rock, Paper, Scissors")
# print(f"{rock}. Rock")
# print(f"{paper}. Paper")
# print(f"{scissors}. Scissors")

# choice = int(input("Choose an option (1-3): "))

# if choice == rock:
#     print("You chose Rock!")
# elif choice == paper:
#     print("You chose Paper!")
# elif choice == scissors:
#     print("You chose Scissors!")
# else:
#     print("Invalid choice.")
    
# Create user input for rps
# Users will be prompted for an input ranging from 1 - 3
# So 1 is for rock
# 2 is for paper
# 3 is for scissors
# Output users input
# Compare users input against users input


# User_choice = input ("choose Rock, Paper, or Scissors: ")

# rock = 1
# paper = 2
# scissors = 3

# # Get input from to diifrent users
# player1 = input("Player 1, choose rock, paper, or scissors: ")
# player2 = input("Player 2, choose rock, paper, or scissors: ")

# # Now to compare the both 
# if player1 == player2:
#     print("It's a tie!")

# # Check all conditions if Player 1 wins
# elif (player1 == "rock" and player2 == "scissors") or \
#      (player1 == "paper" and player2 == "rock") or \
#      (player1 == "scissors" and player2 == "paper"):
#     print("Player 1 wins!")

# # If it's not a tie and Player 1 didn't win, Then Player 2 must have won
# else:
#     print("Player 2 wins!")


# WHAT IS A SET
# It is  a collection of unique items in python, it cannot be duplicated 
# numbers = {0, 1, 2, 3, 4}
# numbers.remove(5)
# print(numbers)
# numbers.discard(10) #it won't show any error even if value does not exsist
  
# fruits = {"apple", "banana", "orange"}
# # fruits.add("mango") # And can take only one argument
# fruits.update(["mango", "kiwi", "watermelon"])
# print(fruits)

# # creating an empty set
# my_set = ()
# print(my_set)

# colours = {"red", "green", "purple"}
# print(len(colours))  # lens for checking num of items in a set

# # set operation, helps you compare two sets
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A | B)  # union:combines items from both sets
# print(A & B)  Returns only the item found in both set
# print(A - B)  Returns item in the first set that are not in the second
# print(A ^ B)  Returns item that are in either set, but not in the both


# LOOPS a programming structure that repeats a loop of codes
# forloops
# for number in range(1, 9):
#     print(number)

# LOOPING THROUGH A LIST
# fruits = ["apple", "banana", "mango"]
# for fruits in fruits:
#     print(fruits)

# # MULTIPLICATION TABLE
# for number in range(1, 11):
#     print(10, "x", number, "=", 10 * number)

# WHILE LOOPS REPEATS CODE AS LONG AS A CONDITION IS TRUE.
# number = 1

# while number <= 6:
#     print(number)
#     number = number + 1

# USING BREAK
# for number in range(1, 6):
#     if number == 3:
#         continue
    
#     print(number)

# LOOPING THROUGH SET
# colours = {"red", "green", "blue"}
# for colour in colours:
#     print(colour)

# USING LOOP TO COUNT ITEMS IN A SET
# numbers = {10, 20, 30, 40, 50}

# total = 0

# for number in numbers:
#     total = total + number

# print("Total:", total)



# list = ["apple", "banana", "cherry"]
# print(list)


# list.append("kiwi")
# list.clear()

# list.extend("Harry", "Harmonie", "Ron")

# print(list)