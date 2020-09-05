""" import csv 
filename = 'http://galileoguzman.com/data/covid19_tweets.csv'
Data= f'dataset/{filename}.csv'
with open(filename, mode='r') as csv_file:
    csv_reader =  csv.DictReader(csv_file)


for row in Data:
    print(row) """

import csv
import urllib.request
from io import StringIO

url = 'http://galileoguzman.com/data/covid19_tweets.csv'
respuesta = urllib.request.urlopen(url)
f = StringIO(bytearray(respuesta.read()).decode())
archivo = csv.reader(f)
for filas in archivo:
    print(filas)


