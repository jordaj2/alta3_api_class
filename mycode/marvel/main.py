#!/usr/bin/env python3
"""Marvel Python Client
RZFeeser@alta3.com | Alta3 Research"""

# standard library imports
import argparse  # pull in arguments from CLI
import time  # create time stamps (for our RAND)
import hashlib  # create our md5 hash to pass to dev.marvel.com
import os
from pprint import pprint  # we only want pprint() from the package pprint

# 3rd party imports
import requests  # python3 -m pip install requests

## Define the API here
API = 'http://gateway.marvel.com/v1/public/characters'


## Calculate a hash to pass through to our MARVEL API call
## Marvel API wants md5 calc md5(ts+privateKey+publicKey)
def hashbuilder(rand, privkey, pubkey):
    return hashlib.md5((f"{rand}{privkey}{pubkey}").encode('utf-8')).hexdigest()  # create an MD5 hash of our identifers


## Perform a call to MARVEL Character API
## http://gateway.marvel.com/v1/public/characters
## ?name=Spider-Man&ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150
def marvelcharcall(rand, keyhash, pubkey, lookmeup):
    r = requests.get(
        f"{API}?name={lookmeup}&ts={rand}&apikey={pubkey}&hash={keyhash}")  # send an HTTP GET to this location

    # the marvel APIs are "flakey" at best, so check for a 200 response
    if r.status_code != 200:
        response = None  #
    else:
        response = r.json()

    # return the HTTP response with the JSON removed
    return response


def last_n_of_comics(x, col):
    # get the comics
    max = range(x)
    l = []
    for n in max:
        l.append(col[n]['name'])
    return l


def download_thumbnail(ext:str = '.jpg', dest_path:str ='./', size:str = 'small', uri:str = '', hero_name:str = ''):
    default_path = './'
    sizes = ['small', 'medium', 'xlarge', 'fantastic', 'uncanny', 'incredible']
    response = requests.get(f"{uri}/portrait_{size}.{ext}")
    try:
        sizes.remove(size)
    except ValueError:
        print(f"The size you specified [{size}] is invalid. Attempting to download another image size.")
    if response.status_code == 200:
        try:
            file = open(f"{dest_path}{hero_name}.{ext}", "wb")
            file.write(response.content)
            file.close()
        except Exception as e:
            file = open(f"{default_path}{hero_name}.{ext}", "wb")
            file.write(response.content)
            file.close()

    while response.status_code != 200 and len(size) != 0:
        for i in range(len(sizes)-1):
            print(f"Attempting to download {sizes[i]} image for{hero_name}")
            response = requests.get(f"{uri}/portrait_{sizes[i]}.{ext}")
            print(os.getcwd())
            if response.status_code == 200:
                try:
                    file = open(f"{dest_path}{hero_name}.{ext}", "wb")
                    file.write(response.content)
                    file.close()
                except Exception as e:
                    file = open(f"{default_path}{hero_name}.{ext}", "wb")
                    file.write(response.content)
                    file.close()
                break
    print(response.url)

def character_profile(api_result):
    profiles = []

    for result in api_result['data']['results']:
        profile = {'name': result['name']}
        profile['comics'] = result['comics']['available']
        profile['last_five'] = last_n_of_comics(5, result['comics']['items'])
        profile['events'] = result['events']['available']
        if len(result['description']) > 0:
            profile['backstory'] = result['description']
        else:
            profile['backstory'] = "N/A"
        profile['pic'] = result['thumbnail']
        profiles.append(profile)
    return profiles


def main():
    ## harvest private key
    with open(args.dev) as pkey:
        privkey = pkey.read().rstrip('\n')

    ## harvest public key
    with open(args.pub) as pkey:
        pubkey = pkey.read().rstrip('\n')

    ## create an integer from a float timestamp (for our RAND)
    rand = str(time.time()).rstrip('.')

    ## build hash with hashbuilder(timestamp, privatekey, publickey)
    keyhash = hashbuilder(rand, privkey, pubkey)

    ## call the API with marvelcharcall(timestamp, hash, publickey, character)
    result = marvelcharcall(rand, keyhash, pubkey, args.hero)


    ## display results
    # pprint(result)
    # pprint(character_profile(result))
    profiles = character_profile(result)
    for profile in profiles:
        print(f"Name: {profile['name']}")
        print(f"Backstory: {profile['backstory']}")
        print(f"Comic Appearances: {profile['comics']}")
        print(f"Last 5 Titles:")
        for title in profile['last_five']:
            print(f"\t{title}")
        download_thumbnail(uri=profile['pic']['path'], dest_path='static/', hero_name=profile['name'],ext=profile['pic']['extension'], size=args.size)

## Define arguments to collect
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # This allows us to pass in public and private keys
    parser.add_argument('--dev', help='Provide the /path/to/file.priv containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub containing Marvel public developer key')
    parser.add_argument('--size', help='Provide the size of the character picture to download.', default="uncanny")

    ## This allows us to pass the lookup character
    parser.add_argument('--hero', help='Character to search for within the Marvel universe')
    args = parser.parse_args()
    main()
