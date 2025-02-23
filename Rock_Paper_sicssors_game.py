import random

def computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def winner(computer, player):
    if player == computer:
        return "It's a Tie"

    elif (player == "rock" and computer == "scissors") or \
        (player == "scissors" and computer == "paper") or \
        (player == "paper" and computer == "rock"):
        return "You Win"
    else:
        return "Computer Wins"

def main():
    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        if player_choice == 'quit':
            print("Thanks for playing!")
            break
        elif player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice, try again.")
            continue

        comp_choice = computer_choice()
        print(f"Computer chose: {comp_choice}")
        print(winner(comp_choice, player_choice))

if __name__ == "__main__":
    main()
