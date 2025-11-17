import requests


def get_random_blague():
    api_url = "https://v2.jokeapi.dev/joke/Any?safe-mode"
    reponse = requests.get(api_url)
    data = reponse.json()

    print("La blague aléatoire :")

    # Blague en une seule partie
    if data.get("type") == "single":
        print(data["joke"])

    # Blague en deux parties
    elif data.get("type") == "twopart":
        print(data["setup"])
        print(data["delivery"])


if __name__ == "__main__":

    get_random_blague()
