import random

def get_choice():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  win_conditions = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
  }
  if player == computer:
    return "It's a tie"
  elif computer == win_conditions[player]:
    return f"{player.title()} beats {computer}! You win!"
  else:
    return f"{computer.title()} beats {player}! You lose."

choices = get_choice()
result = check_win(choices["player"], choices["computer"])
print(result)