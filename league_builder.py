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
    exp_yes = []
    exp_no = []

    for player in players:
        if player["Soccer Experience"] == "YES":
            exp_yes.append(player)
        else:
            exp_no.append(player)
    
    for player in exp_yes:
        if len(sharks) != 3:
            sharks.append(player)
        elif len(dragons) != 3:
            dragons.append(player)
        elif len(raptors) != 3:
            raptors.append(player)

    for player in exp_no:
        if len(sharks) != 6:
            sharks.append(player)
        elif len(dragons) != 6:
            dragons.append(player)
        elif len(raptors) != 6:
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
