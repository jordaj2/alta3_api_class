import requests

uri = 'http://api.open-notify.org/astros.json'


def main():
    response = requests.get(uri)

    data = response.json()

    print(f"People in Space: {len(data['people'])}")

    for people in data['people']:
        print(f"{people['name']} is on the {people['craft']}")


if __name__ == "__main__":
    main()
