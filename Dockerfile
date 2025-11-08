# 1️⃣ Image de base
FROM python:3.12-slim

# 2️⃣ Définir le répertoire de travail
WORKDIR /app

# 3️⃣ Copier les fichiers du projet dans le conteneur
COPY . .

# 4️⃣ Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Commande pour lancer le programme
ENTRYPOINT ["python","main.py"]
#CMD ["bitcoin"]
