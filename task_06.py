class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(players):
    if len(players) != 2:
        raise WrongNumberOfPlayersError("WrongNumberOfPlayersError")

    player1, player1_choice = players[0]
    player2, player2_choice = players[1]

    if player1_choice not in ['R', 'P', 'S'] or player2_choice not in ['R', 'P', 'S']:
        raise NoSuchStrategyError("NoSuchStrategyError")

    if player1_choice == player2_choice:
        return f"{player1} {player1_choice}"
    elif (player1_choice == 'R' and player2_choice == 'S') or \
         (player1_choice == 'P' and player2_choice == 'R') or \
         (player1_choice == 'S' and player2_choice == 'P'):
        return f"{player1} {player1_choice}"
    else:
        return f"{player2} {player2_choice}"

try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
except Exception as e:
    print(e)

try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))
except Exception as e:
    print(e)

print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))
