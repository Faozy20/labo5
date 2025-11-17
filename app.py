import requests

API_URL = "https://v2.jokeapi.dev/joke/Any?format=json"


def get_joke():
    """Interroge JokeAPI et renvoie une blague sous forme de texte."""
    response = requests.get(API_URL, timeout=5)
    response.raise_for_status()  # lève une erreur si API KO
    data = response.json()

    # JokeAPI peut renvoyer 2 formats différents
    if data.get("type") == "single":
        return data.get("joke", "Blague indisponible.")
    else:
        setup = data.get("setup", "")
        delivery = data.get("delivery", "")
        return f"{setup} — {delivery}"


def main():
    print("=== JokeAPI Demo ===")
    try:
        joke = get_joke()
        print(joke)
    except Exception as e:
        print(f"Erreur lors de l'appel à l'API : {e}")


if __name__ == "__main__":
    main()
