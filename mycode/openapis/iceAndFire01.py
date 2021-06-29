import requests
import pprint

AOIF = 'https://www.anapioficeandfire.com/api'


def main():
    # send https get to the API of Ice and Fire

    gotresp = requests.get(AOIF)

    # Decode the response
    got_dj = gotresp.json()

    # print the response
    pprint.pprint(got_dj)


if __name__ == "__main__":
    main()
