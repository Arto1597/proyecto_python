import csv
from datetime import datetime
import requests

Url='http://galileoguzman.com/data/covid19_tweets.csv'
data= "covid"

def descarga(url):

    response = requests.get(url)
    
    if response.status_code == 200:
        response_content = response.content
        filename = f'dataset/{data}.csv'
        with open(filename, 'wb') as csv:
            csv.write(response_content)
            return filename
    return None
