import csv
soccer_csv = "soccer_players.csv"


def file_reader(soccer_file):
    with open(soccer_file, newline = '') as file:
        art_reader = csv.DictReader(file)
        rows = list(art_reader)
        for row in rows:
            print(row)

if __name__ == "__main__":
    file_reader(soccer_csv)