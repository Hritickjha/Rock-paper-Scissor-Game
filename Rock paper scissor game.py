"""""
workflow of project:
1- imput from user (Rock, paper Scissor)
2- Computer Choice(computer will choose randomly not conditionally)
3- Result print

cases:
A-Rock
Rock - Rock = tie
Rock - paper = paper win
Rock - scissor = Rock win

B-paper
paper - paper = tie
paper - Rock = paper win
paper - scissor = scissor win

c-scissor
scissor - scissor = tie
scissor - Rock = Rock win
scissor - paper = scissor win

"""
import random
item_list = ["Rock","paper","scissor"]
user_Choice = input("Enter your move = Rock, paper, Scissor= ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_Choice}, Computer choice = {comp_choice}")

if user_Choice == comp_choice:
    print("Both Chooses Same: = Mathc Tie")
    
elif user_Choice == "Rock":
    if comp_choice == "paper":
        print("paper covers Rock = Computer Win")
    else:
        print("Rock smashes scissor = you win")
elif user_Choice == "paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper, computer win")
    else:
        print("paper covers rock, you win")
elif user_Choice == "scissor":
    if comp_choice == "paper":
        print("Scissor cuts paper, you win")
    else:
        print("Rock smashes scissor, computer win")
  
