import csv
soccer_csv = "soccer_players.csv"

if __name__ == "__main__":
    pass


def file_reader(soccer_file):
    with open(soccer_file, newline = '') as file:
        art_reader = csv.DictReader(file, delimeter = ",")
        rows = list(art_reader)
        for row in rows:
            print(row)

file_reader(soccer_csv)