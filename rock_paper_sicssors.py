import random

choices = ["rock","paper","scissors"]

player_choice = input("Enter Rock,Paper or Scissors: ").lower()
computer_choice = random.choice(choices)

print(f"Player Choice {player_choice}")
print(f"Computer Choice {computer_choice}")

if(player_choice == computer_choice):
    print("It's Tie! ")
elif((player_choice == "rock" and computer_choice == "scissors")
    or
    (player_choice == "paper" and computer_choice == "scissors")
    or
    (player_choice == "scissors" and computer_choice == "paper")
    or(player_choice == "paper" and computer_choice == "rock")
    ):
    print("Player Win")
else:
    print("Computer Wins")        
