from datetime import datetime
import requests
import csv
# CONSTANTS
URL_BASE='http://galileoguzman.com/data/covid19_tweets.csv'
# FUNTIONS
def get_github_user(username):
    url = f'{URL_BASE}users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
def download_user_avatar(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        response_content = response.content
        filename = f'dataset/{csv_filename()}.csv'
        with open(filename, 'wb') as csv_file:
             csv_reader = csv.reader(csv_file)
             for row in csv_reader:
                 print(row)
            return filename
    return None
def image_filename():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return timestamp

download_user_avatar(URL_BASE)