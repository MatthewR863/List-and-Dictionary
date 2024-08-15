# Name: Matthew Reynolds # Date: 03/24/2024
# Class: Comp 163 #Section:002

# Description: Program that stores roster and rating information

# Empty dictionary that stores player information
roster = {}
for i in range(1, 6):
    player_number = int(input(f"Enter player {i}'s jersey number: "))
    player_rating = int(input(f"Enter player {i}'s rating: "))
    roster[player_number] = player_rating

print("ROSTER")
for player_number, player_rating in sorted(roster.items()):
    print(f"Jersey number: {player_number}, Rating: {player_rating}")

def menu():
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output Roster")
    print("q - Quit")
# Add players to roster
player_number = 1
def Add_Player():
    global player_number
    global roster
    jersey = int(input(f"Enter Player {player_number}'s Number: "))
    rating = int(input(f"Enter Player {player_number}'s rating: "))
    roster[jersey] = rating
    player_number += 1
# Removes players from roster
def RemovePlayer():
    jersey = int(input("Enter a jersey number: "))
    if jersey in roster:
        del roster[jersey]

def UpdateRating():
    jersey = int(input("Enter jersey number: "))
    if jersey in roster:
        new_rating = int(input(f"Enter a new rating for Player {jersey}: "))
        roster[jersey] = new_rating
# Outputs players above a certain rating
def PlayersAbove_rating(team_roster):
    rating_threshold = int(input("Enter a rating to see players above: "))
    print(f"ABOVE {rating_threshold}")
    for player_number, player_rating in team_roster.items():
        if player_rating > rating_threshold:
            print(f"Jersey number: {player_number}, Rating: {player_rating}")
def output_roster():
    print("Roster")
    for jersey in sorted(roster.keys()):
        print(f"Jersey Number: {jersey}, Rating: {roster[jersey]}")


# Displays menu after adding players
while True:
    menu()
    player_roster = input("Select an option from the menu: ")

    if player_roster == 'a':
        Add_Player()
    elif player_roster == 'd':
        RemovePlayer()
    elif player_roster == 'u':
        UpdateRating()
    elif player_roster == 'r':
        PlayersAbove_rating(roster)
    elif player_roster == 'o':
        output_roster()
    elif player_roster == 'q':
        break
