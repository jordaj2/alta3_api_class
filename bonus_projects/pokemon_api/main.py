import requests

uri = 'https://pokeapi.co/api/v2/pokemon'
limit = input("Enter a limit on the # of records to return: ")
offset = input("Enter an offset value: ")
query_parameters = f"limit={limit}&offset={offset}"

r = requests.get("{}?{}".format(uri,query_parameters))
print(r.json())
