import os
import sys
import requests

def fetch_joke(category: str = "Any") -> str:
    url = f"https://v2.jokeapi.dev/joke/{category}?type=single&safe-mode"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    data = r.json()
    if data.get("error"):
        # JokeAPI renvoie parfois 'error': true avec un message
        raise RuntimeError(data.get("message", "API returned an error"))
    return data.get("joke", "(no joke returned)")

if __name__ == "__main__":
    category = os.getenv("CATEGORY") or (sys.argv[1] if len(sys.argv) > 1 else "Any")
    try:
        joke = fetch_joke(category)
        print(joke)
    except Exception as e:
        print(f"Erreur: {e}", file=sys.stderr)
        sys.exit(1)
