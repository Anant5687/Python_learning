import random

def get_choice():
    player_choice = input("Enter a choice from rock, paper, scissors:")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


values = get_choice()

def get_winner(player, computer):
    print(f"You chossen {player}, computer chooses {computer}")

    if player == 'rock' and computer == 'rock':
        return "It's a tie!"
    elif player == 'rock':
        if computer == "paper":
            return "Paper covers rock, you lose"
        else:
            return "Rock smasshes scissors, you win!"
    elif player == 'paper':
        if computer == "rock":
            return "Paper covers rock, you win"
        else:
            return  "Rock smasshes paper, you lose!"
    elif player == 'sccisor':
        if computer == "rock":
            return "Rock smasshes pscissor you lose"
        else:
            return  "Scissor cuts paper, you win!"
        

win = get_winner(values["player"], values["computer"])
print(win)