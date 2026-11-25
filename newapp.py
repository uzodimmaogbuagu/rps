# import sys
# import random
# playerchoice = input("Enter \n \n1 for Rock\n2 for paper\n3 for scissors\n")
# player = int(playerchoice)
# print(f"you choose: {player}")

# if player < 1 or player > 3:
#     sys.exit("Invalid choice, you must choose option between 1 and 3")
    

# options = [1, 2, 3]

# computerchoice = random.choice(options)
# print(f"computer choose {computerchoice}")

# if player == 1 and computerchoice == 3:
#     print("you win")
# elif player == computerchoice:
#     print("Its a draw")
# else:
#     print("computer wins")    



   
# import phonenumbers
# from phonumbers import geocoder 
# import time, random

# def start_phone_tracker(target):
#     print(f"[+] phoneTracer v2.1 . OSINT")
#     print(f"[*] Target: {target}!")
#     print(f"[*] Initilaizing trace...")
#     p = phonenumbers.parse(target. None)
#     r = geocoder.description_fo_number(p)
#     print(f"[+] Location; {r}")
#     print(f"[+] TRace commplete")
    
# start_phone_tracker("+234-813-135-5-757")

    
    
# import turtle
# import math

# t = turtle. Turtle()
# t.speed(0)
# t.color("red")
# turtle.bgcolor("black")

# def corazon(n):
#     x = 16 * math.sin(n) ** 3
#     y = 13 * math.cos(n) - 5 * math.cos(
#         2*n) - 2*math.cos(3*n) - math.cos(4*n)
#     return x, y

# t.penup()
# for i in range(15):
#     t.goto(0, 0)
#     t.pendown()
#     for n in range(0, 100, 2):
#         x, y = corazon(n/10)
#         t.goto(x=1, y =1)
#     t.penup()
    
# t.hideturtle()
# turtle.done()
