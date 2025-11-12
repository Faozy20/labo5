# ue19-lab-05 — Mini app Python + Docker (requests + JokesAPI)

Cette application Python 3 interroge l'API publique **JokeAPI** pour afficher une blague.
Aucune clé n'est nécessaire.

---

## Fichiers
- `app.py` : code Python qui interroge l'API via `requests`.
- `requirements.txt` : dépendances du projet.
- `Dockerfile` : image Docker minimaliste pour exécuter `app.py`.
- `README.md` : ce guide.

## Prérequis (exécution locale)
- Python 3.10+
- `pip`

## Installation & exécution (local)
```bash
python -m venv .venv
source .venv/bin/activate  # sous Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Lancer
python app.py
# Catégorie optionnelle (Any, Programming, Misc, Dark, Pun, Spooky, Christmas)
python app.py Programming

# Ou via variable d'environnement
CATEGORY=Programming python app.py
```

## Exécution avec Docker
```bash
docker build -t ue19-lab-05:latest .
docker run --rm ue19-lab-05
# Avec une catégorie spécifique
docker run --rm -e CATEGORY=Programming ue19-lab-05
```

## Détails API
- Endpoint utilisé : `https://v2.jokeapi.dev/joke/<CATEGORY>?type=single&safe-mode`
  (ex: `CATEGORY=Any`).
- La réponse JSON contient au moins le champ `joke` quand `type=single`.

## Dépannage
- Proxy/Firewall : assurez-vous d'avoir un accès Internet sortant.
- L'app affiche les erreurs HTTP/JSON sur `stderr` et renvoie un code de sortie `1` en cas d'échec.

## Comment publier sur GitHub
```bash
git init
git add .
git commit -m "ue19-lab-05: Python requests + Docker + JokeAPI"
gh repo create ue19-lab-05 --public --source=. --remote=origin --push
# Sinon avec Git classique :
# 1) créer le repo public vide "ue19-lab-05" sur GitHub
# 2) git remote add origin <URL_DU_REPO>
# 3) git push -u origin main
```
