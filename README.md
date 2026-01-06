# Exercice 6 – Docker Compose

## Objectif
Déployer une application Flask connectée à une base de données MongoDB avec Docker Compose.

## Contenu
Le projet contient deux services :
- une application Flask
- une base de données MongoDB

## Fichiers
- app.py  
- requirements.txt  
- Dockerfile  
- docker-compose.yml  

## Lancement
Depuis le répertoire du projet, exécuter :
  
docker compose up --build

## Vérification
L’application Flask expose une route permettant de vérifier la connexion à MongoDB.

Dans un navigateur :
  
http://localhost:5002/healthz

Résultat attendu :
  
MongoDB: OK

Ce résultat confirme que la connexion à la base de données est fonctionnelle.

## Arrêt
Pour arrêter les conteneurs :
  
docker compose down
