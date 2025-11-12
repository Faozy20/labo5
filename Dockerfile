FROM python:3.12-slim

# Empêche l'écriture de fichiers pyc et force des logs non bufferisés
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Par défaut : lance l'app
CMD ["python", "app.py"]
