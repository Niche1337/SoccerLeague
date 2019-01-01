import csv
SOCCER_CSV = "soccer_players.csv"

#Going for exceeds expectation

def file_reader(soccer_file):
    '''The file reader creates a list of ordered dictionaries, of all the  players in the soccer.csv file.
    It takes a csv file as an argument
    '''
    players = []
    with open(soccer_file, newline = '') as file:
        art_reader = csv.DictReader(file)
        players = list(art_reader)     
    return players

def team_creator(players):
    sharks = []
    dragons = []
    raptors = []
    exp_yes = []
    exp_no = []
    '''The team creator function splits the players from the soccer.csv, 
        into three evenly distrubted teams based on soccer experience
        It takes a list containing the players, and return three even distributed lists
    '''
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
    '''Takes three teams, containing players, and creats a teams.txt file
    '''
    with open("teams.txt", "w") as file:
        team_names = ["Sharks", "Dragons", "Raptors"]
        for name in team_names:
            file.write(("{}\n".format(name)))
            if name == "Sharks":
                player_letter(team1, team_names[0])
                for players in team1:
                    file.write("{}, {}, {}\n".format(players["Name"], players["Soccer Experience"], players["Guardian Name(s)"]))
                file.write("-"*40 + "\n"*3)
            elif name == "Dragons":
                player_letter(team2, team_names[1])
                for players in team2:
                    file.write("{}, {}, {}\n".format(players["Name"], players["Soccer Experience"], players["Guardian Name(s)"]))
                file.write("-"*40 + "\n"*3)
            elif name == "Raptors":
                player_letter(team3,team_names[2])
                for players in team3:
                    file.write("{}, {}, {}\n".format(players["Name"], players["Soccer Experience"], players["Guardian Name(s)"]))
                file.write("-"*40 + "\n"*3)

def player_letter(soccer_file, team_name):
    '''Takes the one of the teams list of players, and the name of the team.
    return a welcoming text file
    '''
    for player in soccer_file:        
        player_name = player["Name"].split()
        with open("{}_{}.txt".format(player_name[0], player_name[1]), "w") as file:        
                file.write("Dear {}\n\t {} has been assigned to the team {},\n the date and time of the first practise is 02/02/2019, 09.00".format(player["Guardian Name(s)"], player["Name"], team_name))



if __name__ == "__main__":
    players = file_reader(SOCCER_CSV)
    sharks, dragons, raptors = team_creator(players)
    team_file_creator(sharks, dragons, raptors)

