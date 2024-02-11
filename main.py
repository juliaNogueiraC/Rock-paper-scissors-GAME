import random

choices = ["rock", "paper", "scissors"]

# Randomly choose computer's choice
computer = random.choice(choices)

# Get valid player input using a loop
while True:
    player = input("Rock, paper, or scissors? ").lower()
    if player in choices:
        break
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")

# Display choices and winner
print("Computer chose:", computer)
print("Player chose:", player)

# Determine winner using concise logic
winner = {
    "rock": ["scissors"],
    "paper": ["rock"],
    "scissors": ["paper"]
}[computer]

if player in winner:
    print("You win!")
elif player == computer:
    print("It's a tie!")
else:
    print("You lose!")



# ... (rest of your code) ...

# Perguntar se quer jogar novamente
again = None
while again not in ("s", "n"):
    again = input("Deseja jogar novamente? (s/n) ").lower()

# Reiniciar o jogo se o usuário digitar "s"
if again == "s":
    main()
else:
    print("Obrigado por jogar!")
