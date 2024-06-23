import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def main():
    user_score = 0
    computer_score = 0

    while True:
        
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        
        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            print("You win this round!")
            user_score += 1
        elif winner == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")

        
        print(f"Scores: You - {user_score}, Computer - {computer_score}")

        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing! Final scores:")
    print(f"You: {user_score}, Computer: {computer_score}")


if __name__ == "__main__":
    main()
