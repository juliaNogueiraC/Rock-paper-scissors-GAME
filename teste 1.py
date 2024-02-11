import random

choices = ["rock","paper","scissors"]

computer = random.choices(choices)
player = None 
#print(computer)
# to prevent the player choose a choice is not right
while player not in choices:
  player = input("rock, paper, or scissors?").lower()

# to compare the player and computer choice
if player == computer:
  print("computer: ",computer)
  print("player: ",player)
  print("Tie!")
  
elif player == "rock":
  if computer == "paper":
    print("computer: ",computer)
    print("player: ",player)
    print("You lose!")
  if computer == "scissors":
    print("computer: ",computer)
    print("player: ",player)
    print("You win!")
    
elif player == "scissors":
  if computer == "rock":
    print("computer: ",computer)
    print("player: ",player)
    print("You lose!")
  if computer == "paper":
    print("computer: ",computer)
    print("player: ",player)
    print("You win!")
    
elif player == "paper":
  if computer == "scissors":
    print("computer: ",computer)
    print("player: ",player)
    print("You lose!")
  if computer == "rock":
    print("computer: ",computer)
    print("player: ",player)
    print("You win!")
    
    


print("computer chose", computer)
print("player chose", player)