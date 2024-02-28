import random

def roll():
    min_value = 1
    max_value = 6

    roll = random(min_value, max_value)

    value = roll()
    print(value)

    
while True:
    players = input("Enter the number of player(2-4): ")
    if players.isdigit():
        players = int(players)    
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
            print("invalid, try again.")


max_score = 50
player_scores = [0 for_in range(players)]

while max(player_scores) < max_score:
     for player_idx in range(players):
          print("\nPlayer number", player_idx + 1, "trun has just started!\n")
          current_score = 0

          while True:
               should_roll = input("would you like to roll (y)? ")
               if should_roll.lower() !="y":
                    break
               
               value = roll()
               if value == 1:
                    print("you rolled a 1! turn done!")
                    current_score = 0
                    break
               else:
                    current_score += value
                    print("you rolled a: ", value)

               print("your score is:", current_score)

          player_scores[player_idx] += current_score
          print("your total score is:", player_scores[player_idx])
             
                   
