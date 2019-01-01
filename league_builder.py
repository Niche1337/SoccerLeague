import csv
SOCCER_CSV = "soccer_players.csv"


def file_reader(soccer_file):
    rows = []
    with open(soccer_file, newline = '') as file:
        art_reader = csv.DictReader(file)
        rows = list(art_reader)     
    return rows

def team_creator(players):
    sharks = []
    dragons = []
    raptors = []
    #sharks.append([shark for shark in players if shark["Soccer Experience"] == "YES"] )
    # for player in players:
    #     if player["Soccer Experience"] == "YES" and len(sharks) < 4:     
    #         sharks.append(player)
    #     elif player["Soccer Experience"] == "YES" and len(dragons) < 4:
    #         dragons.append(player)
    #     elif player["Soccer Experience"] == "YES" and len(raptors) < 4:
    #         raptors.append(player)        
    #     elif player["Soccer Experience"] == "NO" and len(sharks) != 6:     
    #         sharks.append(player)
    #     elif player["Soccer Experience"] == "NO" and len(dragons) != 6:
    #         dragons.append(player)
    #     elif player["Soccer Experience"] == "NO" and len(raptors) != 6:
    #         raptors.append(player)

    for player in players:
        if player["Soccer Experience"] == "YES" and len(sharks) < 4:     
            sharks.append(player)
        elif player["Soccer Experience"] == "YES" and len(dragons) < 4:
            dragons.append(player)
        elif player["Soccer Experience"] == "YES" and len(raptors) < 4:
            raptors.append(player)
    
    for player in players:
        if player["Soccer Experience"] == "NO" and len(sharks) < 6:     
            sharks.append(player)
        elif player["Soccer Experience"] == "NO" and len(dragons) < 6:
            dragons.append(player)
        elif player["Soccer Experience"] == "NO" and len(raptors) < 6:
            raptors.append(player)
    
    return sharks, dragons, raptors


def team_file_creator(team1, team2, team3):
    with open("teams.txt", "w") as file:
        team_names = ["Sharks", "Dragons", "Raptors"]
        for name in team_names:
            file.write(("{}\n".format(name)))
            if name == "Sharks":
                for players in team1:
                    file.write("{}, {}, {}\n".format(players["Name"], players["Soccer Experience"], players["Guardian Name(s)"]))
                file.write("-"*40 + "\n"*3)
            elif name == "Dragons":
                for players in team2:
                    file.write("{}, {}, {}\n".format(players["Name"], players["Soccer Experience"], players["Guardian Name(s)"]))
                file.write("-"*40 + "\n"*3)
            elif name == "Raptors":
                for players in team3:
                    file.write("{}, {}, {}\n".format(players["Name"], players["Soccer Experience"], players["Guardian Name(s)"]))
                file.write("-"*40 + "\n"*3)
            



if __name__ == "__main__":
    players = file_reader(SOCCER_CSV)
    sharks, dragons, raptors = team_creator(players)
    team_file_creator(sharks, dragons, raptors)
## TODO write up team file writer 