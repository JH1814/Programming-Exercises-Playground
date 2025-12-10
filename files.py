import csv

def main():
    file = open("./names.txt", "r")
    for line in file:
        line = line.strip("\n")
        first_name, birthyear = line.split(" ")
        print(f"{first_name} was born in {birthyear}.")
    file.close()

    with open("./names_birthdates.csv", "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            first_name, birthdate = row
            print(f"{first_name} was born on {birthdate}.")
main()