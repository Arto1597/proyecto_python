import csv

Filename = 'covid.csv'
with open(Filename, mode =  "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader: 
        print(row)