import csv
soccer_csv = "soccer_players.csv"
sharks = []
dragons = []
raptors = []

def file_reader(soccer_file):
    rows = []
    with open(soccer_file, newline = '') as file:
        art_reader = csv.DictReader(file)
        rows = list(art_reader)
        #
    return rows

def team_creator(players):

    #sharks.append([shark for shark in players if shark["Soccer Experience"] == "YES"] )
    for player in players:
        if player["Soccer Experience"] == "YES" and len(sharks) < 4:     
            sharks.append(player)
        elif player["Soccer Experience"] == "YES" and len(dragons) < 4:
            dragons.append(player)
        elif player["Soccer Experience"] == "YES" and len(raptors) < 4:
            raptors.append(player)        
        elif player["Soccer Experience"] == "NO" and len(sharks) != 6:     
            sharks.append(player)
        elif player["Soccer Experience"] == "NO" and len(dragons) != 6:
            dragons.append(player)
        elif player["Soccer Experience"] == "NO" and len(raptors) != 6:
            raptors.append(player)
        



    print(sharks)
    print(dragons)
    print(raptors)



def team_file_creator(team1, team2, team3):
    with open("teams.txt", "a") as file:
        file.writelines(("This is a test"))


if __name__ == "__main__":
    players = file_reader(soccer_csv)
    team_creator(players)

##TODO write up team creator func
## TODO write up team file writer 