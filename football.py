print('Welcome to football predictor')
print('Enter results for last 5 games of each team to generate predictions')
print('---'*10)
print('Matches will be in order from newest one to oldest one')

team1_points = []
team2_points = []


# Point system for AWAY matches
first_away_win = 10.5      # 10.5 points for a win
first_away_draw = 7.5      # 7.5 points for a draw
first_away_loss = 4        # 4 points for a loss

second_away_win = 9        # 9 points for a win
second_away_draw = 6       # 6 points for a draw
second_away_loss = 3       # 3 points for a loss

third_away_win = 7.5       # 7.5 points for a win
third_away_draw = 4.5      # 4.5 points for a draw
third_away_loss = 2        # 2 points for a loss

fourth_away_win = 6        # 6 points for a win
fourth_away_draw = 3       # 3 points for a draw
fourth_away_loss = 1           # 1 points for a loss

fifth_away_win = 4.5       # 4.5 points for a win
fifth_away_draw = 1.5      # 1.5 points for a draw
fifth_away_loss = 0        # 0 points for a loss

# Point system for HOME matches
first_home_win = 9.5       # 9.5 points for a win
first_home_draw = 7        # 7 points for a draw
first_home_loss = 3        # 3 points for a loss

second_home_win = 8        #8 points for a win
second_home_draw = 5       #5 points for a draw
second_home_loss = 2       #2 points for a loss

third_home_win = 6.5       #6.5 points for a win
third_home_draw = 3.5      #3.5 points for a draw
third_home_loss = 1        #1 points for a loss

fourth_home_win = 5        #5 points for a win
fourth_home_draw = 2       #2 points for a draw
fourth_home_loss = 0       #0 points for a loss

fifth_home_win = 3.5       #3.5 points for a win
fifth_home_draw = 1        #1 points for a draw
fifth_home_loss = 0        #0 points for a loss

#TEAM 1
#MATCH 1
team1_name = input("Please give  Home Team name: ")
match1 = input(f"MATCH 1 - {team1_name}\nSelect:\nHome Game(type 'H')\nAway Game('type 'A'): ")
result1 = input('Enter Result:\nWin(enter "W"),\nLoss(enter "L")\nDraw(enter "D"): ')
if match1 == 'H' or match1 == 'h':
    if result1 == 'W' or result1 == 'w':
        team1_points.append(first_home_win)
    elif result1 == 'D' or result1 == 'd':
        team1_points.append(first_home_draw)
    else:
        team1_points.append(first_home_loss)
if match1 == 'A' or match1 == 'a':
    if result1 == 'W' or result1 == 'w':
        team1_points.append(first_away_win)
    elif result1 == 'D' or result1 == 'd':
        team1_points.append(first_away_draw)
    else:
        team1_points.append(first_away_loss)
print('---')
#MATCH 2
match2 = input(f"MATCH 2 - {team1_name}\nSelect:\nHome Game(type 'H')\nAway Game('type 'A'): ")
result2 = input('Enter Result:\nWin(enter "W"),\nLoss(enter "L")\nDraw(enter "D"): ')
if match2 == 'H' or match2 == 'h':
    if result2 == 'W' or result2 == 'w':
        team1_points.append(second_home_win)
    elif result2 == 'D' or result2 == 'd':
        team1_points.append(second_home_draw)
    else:
        team1_points.append(second_home_loss)
if match2 == 'A' or match2 == 'a':
    if result2 == 'W' or result2 == 'w':
        team1_points.append(second_away_win)
    elif result2 == 'D' or result2 == 'd':
        team1_points.append(second_away_draw)
    else:
        team1_points.append(second_away_loss)
print('---')
#MATCH 3
match3 = input(f"MATCH 3 - {team1_name}\nSelect:\nHome Game(type 'H')\nAway Game('type 'A'): ")
result3 = input('Enter Result:\nWin(enter "W"),\nLoss(enter "L")\nDraw(enter "D"): ')
if match3 == 'H' or match3 == 'h':
    if result3 == 'W' or result3 == 'w':
        team1_points.append(third_home_win)
    elif result3 == 'D' or result3 == 'd':
        team1_points.append(third_home_draw)
    else:
        team1_points.append(third_home_loss)
if match3 == 'A' or match3 == 'a':
    if result3 == 'W' or result3 == 'w':
        team1_points.append(third_away_win)
    elif result3 == 'D' or result3 == 'd':
        team1_points.append(third_away_draw)
    else:
        team1_points.append(third_away_loss)
print('---')
#MATCH 4
match4= input(f"MATCH 4 - {team1_name}\nSelect:\nHome Game(type 'H')\nAway Game('type 'A'): ")
result4 = input('Enter Result:\nWin(enter "W"),\nLoss(enter "L")\nDraw(enter "D"): ')
if match4 == 'H' or match4 == 'h':
    if result4 == 'W' or result4 == 'w':
        team1_points.append(fourth_home_win)
    elif result4 == 'D' or result4 == 'd':
        team1_points.append(fourth_home_draw)
    else:
        team1_points.append(fourth_home_loss)
if match4 == 'A' or match4 == 'a':
    if result4 == 'W' or result4 == 'w':
        team1_points.append(fourth_away_win)
    elif result4 == 'D' or result4 == 'd':
        team1_points.append(fourth_away_draw)
    else:
        team1_points.append(fourth_away_loss)
print('---')
#MATCH 5
match5= input(f"MATCH 5 - {team1_name}\nSelect:\nHome Game(type 'H')\nAway Game('type 'A'): ")
result5 = input('Enter Result:\nWin(enter "W"),\nLoss(enter "L")\nDraw(enter "D"): ')
if match4 == 'H' or match4 == 'h':
    if result5 == 'W' or result5 == 'w':
        team1_points.append(fifth_home_win)
    elif result5 == 'D' or result5 == 'd':
        team1_points.append(fifth_home_draw)
    else:
        team1_points.append(fifth_home_loss)
if match4 == 'A' or match4 == 'a':
    if result5 == 'W' or result5 == 'w':
        team1_points.append(fifth_away_win)
    elif result5 == 'D' or result5 == 'd':
        team1_points.append(fifth_away_draw)
    else:
        team1_points.append(fifth_away_loss)
print('---'*10)
#TEAM 2
# MATCH 1
team2_name = input("Please give Away Team name: ")
match1 = input(f"MATCH 1 - {team2_name}\nSelect:\nHome Game(type 'H')\nAway Game('type 'A'): ")
result1 = input('Enter Result:\nWin(enter "W"),\nLoss(enter "L")\nDraw(enter "D"): ')
if match1 == 'H' or match1 == 'h':
    if result1 == 'W' or result1 == 'w':
        team2_points.append(first_home_win)
    elif result1 == 'D' or result1 == 'd':
        team2_points.append(first_home_draw)
    else:
        team2_points.append(first_home_loss)
if match1 == 'A' or match1 == 'a':
    if result1 == 'W' or result1 == 'w':
        team2_points.append(first_away_win)
    elif result1 == 'D' or result1 == 'd':
        team2_points.append(first_away_draw)
    else:
        team2_points.append(first_away_loss)
print('---')
# MATCH 2
match2 = input(f"MATCH 2 - {team2_name}\nSelect:\nHome Game(type 'H')\nAway Game('type 'A'): ")
result2 = input('Enter Result:\nWin(enter "W"),\nLoss(enter "L")\nDraw(enter "D"): ')
if match2 == 'H' or match2 == 'h':
    if result2 == 'W' or result2 == 'w':
        team2_points.append(second_home_win)
    elif result2 == 'D' or result2 == 'd':
        team2_points.append(second_home_draw)
    else:
        team2_points.append(second_home_loss)
if match2 == 'A' or match2 == 'a':
    if result2 == 'W' or result2 == 'w':
        team2_points.append(second_away_win)
    elif result2 == 'D' or result2 == 'd':
        team2_points.append(second_away_draw)
    else:
        team2_points.append(second_away_loss)
print('---')
# MATCH 3
match3 = input(f"MATCH 3 - {team2_name}\nSelect:\nHome Game(type 'H')\nAway Game('type 'A'): ")
result3 = input('Enter Result:\nWin(enter "W"),\nLoss(enter "L")\nDraw(enter "D"): ')
if match3 == 'H' or match3 == 'h':
    if result3 == 'W' or result3 == 'w':
        team2_points.append(third_home_win)
    elif result3 == 'D' or result3 == 'd':
        team2_points.append(third_home_draw)
    else:
        team2_points.append(third_home_loss)
if match3 == 'A' or match3 == 'a':
    if result3 == 'W' or result3 == 'w':
        team2_points.append(third_away_win)
    elif result3 == 'D' or result3 == 'd':
        team2_points.append(third_away_draw)
    else:
        team2_points.append(third_away_loss)
print('---')
# MATCH 4
match4 = input(f"MATCH 4 - {team2_name}\nSelect:\nHome Game(type 'H')\nAway Game('type 'A'): ")
result4 = input('Enter Result:\nWin(enter "W"),\nLoss(enter "L")\nDraw(enter "D"): ')
if match4 == 'H' or match4 == 'h':
    if result4 == 'W' or result4 == 'w':
        team2_points.append(fourth_home_win)
    elif result4 == 'D' or result4 == 'd':
        team2_points.append(fourth_home_draw)
    else:
        team2_points.append(fourth_home_loss)
if match4 == 'A' or match4 == 'a':
    if result4 == 'W' or result4 == 'w':
        team2_points.append(fourth_away_win)
    elif result4 == 'D' or result4 == 'd':
        team2_points.append(fourth_away_draw)
    else:
        team2_points.append(fourth_away_loss)
print('---')
# MATCH 5
match5 = input(f"MATCH 5 - {team2_name}\nSelect:\nHome Game(type 'H')\nAway Game('type 'A'): ")
result5 = input('Enter Result:\nWin(enter "W"),\nLoss(enter "L")\nDraw(enter "D"): ')
if match4 == 'H' or match4 == 'h' :
    if result5 == 'W' or result5 == 'w':
        team2_points.append(fifth_home_win)
    elif result5 == 'D' or result5 == 'd':
        team2_points.append(fifth_home_draw)
    else:
        team2_points.append(fifth_home_loss)
if match4 == 'A' or match4 == 'a':
    if result5 == 'W' or result5 == 'w':
        team2_points.append(fifth_away_win)
    elif result5 == 'D' or result5 == 'd':
        team2_points.append(fifth_away_draw)
    else:
        team2_points.append(fifth_away_loss)
print('---')
# print("Team 1 total points: ", sum(team1_points))
# print("Team 2 total points: ", sum(team2_points))

team1_calculated_points = sum(team1_points)
team2_calculated_points = sum(team2_points)

team1_wins = sum(team1_points) - sum(team2_points)
team2_wins = sum(team2_points) - sum(team1_points)

print('---'*10)
if team1_calculated_points > team2_calculated_points:
    print(f'{team1_name} have bigger chance to win this game with {team1_calculated_points} points to compare to {team2_name} with {team2_calculated_points}')
    print(f'There is {team1_wins} points between those teams.')
elif team2_calculated_points > team1_calculated_points:
    print(f'{team2_name} have bigger chance to win this game with {team2_calculated_points} points to compare to {team1_name} with {team1_calculated_points} points')
    print(f'There is {team2_wins} points between those teams.')
else:
    print("Not enough points difference to pick a winner or it might be a draw")
    print(team1_name, team1_calculated_points)
    print(team2_name, team2_calculated_points)

print('---'*10)
print(team1_name, 'SUMMARY: ', team1_points,'=', team1_calculated_points)
print(team2_name, 'SUMMARY: ', team2_points,'=', team2_calculated_points)

# Program was made on 03/02/2024 by Krzysztof Wazydrag

