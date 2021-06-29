import requests
import pprint

AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"


def main():
    # send https get to the API of Ice and Fire

    gotresp = requests.get(AOIF_BOOKS)

    # Decode the response
    got_dj = gotresp.json()

    # loop across response
    for singlebook in got_dj:
        # display the name of each book
        # all of the below statements do the same thing
        # print(singlebook['name'] + ",", "pages -", singlebook["numberOfPages"])
        # print("{}, pages - {}".format(singlebook['name'], singlebook["numberOfPage"]))
        print(f"{singlebook['name']}, pages - {singlebook['numberOfPages']}")
        print(f"\tAPI URL -> {singlebook['url']}\n")
        # print ISBN
        print(f"\tISBN -> {singlebook['isbn']}\n")
        print(f"\tPUBLISHER -> {singlebook['publisher']}\n")
        print(f"\tNo. of CHARACTERS -> {len(singlebook['characters'])}\n")


if __name__ == "__main__":
    main()
