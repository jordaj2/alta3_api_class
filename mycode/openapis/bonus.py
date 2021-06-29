#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint
import random
AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"


def main():

    # Ask user for input
    got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! Enter '0' to exit. ")
    while got_charToLookup != '0':
        # Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(f"{AOIF_CHAR}{got_charToLookup}")
        got_dj = ""

        if got_charToLookup != "0" and gotresp.status_code == 200:
            # Decode the response
            got_dj = gotresp.json()
            pprint.pprint(got_dj)
            print("\n\n")
            if got_dj.get('name') and len(got_dj['name']) > 0:
                print(f"Name: {got_dj['name']}")
                print(f"Alias Count: {len(got_dj['aliases'])}")
            elif len(got_dj['aliases']) > 0:
                # if more than one alias exists and no name return one of the x aliases randomly
                print(f"Name (Alias): {got_dj['aliases'][random.randint(0,(len(got_dj['aliases'])-1))]}")
            char_books = got_dj['books']
            char_allegiances = got_dj['allegiances']
            print(f"Featured Books:")
            for book in char_books:
                b = requests.get(book)
                b_json = b.json()
                print(f"\t{b_json['name']}")
            print(f"Known Allegiances:")
            if len(char_allegiances) == 0:
                print("\t None")
            for allegiance in char_allegiances:
                a = requests.get(allegiance)
                a_json = a.json()
                print(f"\t{a_json['name']}")
            print('\n')

        if got_charToLookup != "0" and gotresp.status_code != 200:
            print(f"Unable to find a character with the ID of {got_charToLookup}. Try again...\n")
        got_charToLookup = input(
            "Pick a number between 1 and 1000 to return info on a GoT character! Enter '0' to exit. ")


if __name__ == "__main__":
    main()
