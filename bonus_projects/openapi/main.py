
import requests
import pprint
import random
import pandas as pd
AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

AOIF_CHAR_PARAMETERS = '?page=1&pageSize=100'


def link_header_to_dict(h):
    paging_dict = {}
    entries = h.split(',')
    for entry in entries:
        paging = entry.split(';')
        paging_dict[paging[1].split('=')[1].replace('"', '')] = paging[0].replace('<', '').replace('>', '')
    return paging_dict


r = requests.get(f"{AOIF_CHAR}{AOIF_CHAR_PARAMETERS}")

paging_data = link_header_to_dict(r.headers['Link'])
data = r.json()
count = 0
characters = []
characters += r.json()
while paging_data.get('next'):
    r = requests.get(paging_data['next'])
    #pprint.pprint(r.json())
    characters += r.json()
    paging_data = link_header_to_dict(r.headers['Link'])

    # we are on the last page
    if not paging_data.get('next') and paging_data.get('last'):
        r = requests.get(paging_data['last'])
        characters += r.json()

    # pprint.pprint(paging_data)

character_panda = pd.json_normalize(characters)
character_panda.query()


def search_characters(df, query):
    return df.query(query)