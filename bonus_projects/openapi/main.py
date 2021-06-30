import requests
import pprint
import random
import pandas as pd

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

AOIF_CHAR_PARAMETERS = '?page=1&pageSize=100'


def search_characters(df, query):
    data_frame = None
    try:
        data_frame = df.query(query)
    except Exception as e:
        print(f"An error occurred performing the query: {query}.\n ERROR {e}")
    if type(data_frame) is None:
        return None
    return data_frame


def link_header_to_dict(h):
    """
    :param h - a response header "Link" string that tells the pagination information for the query
    TURN THE r.headers['Link'] string

    '<https://www.anapioficeandfire.com/api/characters?page=41&pageSize=50>; rel="prev",
     <https://www.anapioficeandfire.com/api/characters?page=1&pageSize=50>; rel="first",
     <https://www.anapioficeandfire.com/api/characters?page=43&pageSize=50>; rel="last"',
     <https://www.anapioficeandfire.com/api/characters?page=42&pageSize=50>; rel="next"'

    INTO THIS
    {'prev': 'https://www.anapioficeandfire.com/api/characters?page=41&pageSize=50',
     'first': ' https://www.anapioficeandfire.com/api/characters?page=1&pageSize=50',
     'last': ' https://www.anapioficeandfire.com/api/characters?page=43&pageSize=50',
     ,'next': 'https://www.anapioficeandfire.com/api/characters?page=42&pageSize=50'
     }

    SO IT CAN BE USE TO LOOP THROUGH ALL THE CHARACTERS
    """

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
    # pprint.pprint(r.json())
    characters += r.json()
    paging_data = link_header_to_dict(r.headers['Link'])

    # we are on the last page
    if not paging_data.get('next') and paging_data.get('last'):
        r = requests.get(paging_data['last'])
        characters += r.json()

    # pprint.pprint(paging_data)

character_panda = pd.json_normalize(characters)

query = ""

while query != "!!":
    # tested the query: gender =="Female"
    # tested the query: died.str.contains("AC", na=False) # na for NaN values which contains does not work on unless
    #                   this flag is applied.
    result = search_characters(character_panda, input("Enter query string for GoT characters: (Enter !! to exit) :  "))
    if type(result) is not None:
        pprint.pprint(result.to_dict())
