player1_games = []
player2_games = []

player1_wins = 0
player2_wins = 0
draws = 0

with open("player1.txt", "r") as file:

    player1_games = file.readlines()

with open("player2.txt", "r") as file:

    player2_games = file.readlines()

for game in range(len(player1_games)):

    player1_descision = player1_games[game].strip()
    player2_descision = player2_games[game].strip()

    if player1_descision == player2_descision:
        draws += 1
    elif player1_descision == "R" and player2_descision == "S":
        player1_wins += 1
    elif player1_descision == "S" and player2_descision == "P":
        player1_wins += 1
    elif player1_descision == "P" and player2_descision == "R":
        player1_wins += 1
    else:
        player2_wins += 1

with open("result.txt", "w") as file:

    file.write(f"Player1 wins: {str(player1_wins)}\n")
    file.write(f"Player2 wins: {str(player2_wins)}\n")
    file.write(f"Draws: {str(draws)}\n")
    