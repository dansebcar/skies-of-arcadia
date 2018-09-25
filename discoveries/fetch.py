import json
import re

from bs4 import BeautifulSoup
import requests

url = 'http://skiesofarcadia.wikia.com/'
response = requests.get(f'{url}/wiki/Discoveries')
soup = BeautifulSoup(response.text, 'html.parser')
content = soup.find(id='mw-content-text')
both_games = True
discoveries = {}

for el in content.find_all(['span', 'li']):
    if el.name == 'li':
        m = re.search('\d+', el.text)

        if m:
            index = m.group(0)
            a = el.find('a')

            discoveries[index] = {
                'name': a.text,
                'href': f'{url}{a["href"]}',
                'both': both_games,
            }
    elif el.name == 'span':
        if 'id' in el and el['id'] == 'Legends_Exclusives':
            both_games = False


print(f'Fetched {len(discoveries)} discoveries')


with open('fetched-discoveries.json', 'w') as f:
    json.dump(discoveries, f)
