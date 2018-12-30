import csv
soccer_csv = "soccer_players.csv"


def file_reader(soccer_file):
    rows = []
    with open(soccer_file, newline = '') as file:
        art_reader = csv.DictReader(file)
        rows = list(art_reader)
        #
    return rows

def team_creator(players):
    sharks = []
    dragons = []
    raptors = []

    print(players[0]['Name'])

    sharks.append([shark for shark in players if shark["Soccer Experience"] == "YES"] )

    
    print(sharks[0][0]["Name"])



def team_file_creator(team1, team2, team3):
    with open("teams.txt", "a") as file:
        file.writelines(("This is a test"))


if __name__ == "__main__":
    players = file_reader(soccer_csv)
    team_creator(players)

##TODO write up team creator func
## TODO write up team file writer 