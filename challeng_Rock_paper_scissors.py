import random

choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = True
cpu_score = 0
player_score = 0

while True:
    player = input("Rock ,Paper , Scissors")
    player.capitalize()

    if  player == "Scissors" and computer == "Scissors"    :
        print("=")
    if player == "Scissors" and computer =="paper":
        print("Player is winner")
        player_score+=1
    if player == "Scissors" and computer =="Rock":
        print("cpu is winner")
        cpu_score+=1

    if player == "Rock"and computer =="Rock":
        print("=")
    if player=="Rock"and computer =="Scissors":
        print("Player is winner")
        player_score+=1
    if player=="Rock"and computer =="Paper":
        print("cpu is winner")
        cpu_score+=1

    if player=="Paper"and computer =="Paper":
        print("=")
    if player=="Paper"and computer =="Rock":
        print("Player is winner")
        player_score+=1
    if player=="Paper"and computer =="Scissors":
        print("cpu is winner")
        cpu_score+=1

    elif player == 'End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Player:{player_score}")
        break




