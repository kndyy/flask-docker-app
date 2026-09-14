# flask-docker-app

Aplicacion Flask mas PostgreSQL con Docker Compose para el laboratorio 5.2.

## Contenido

app.py
requirements.txt
Dockerfile
.dockerignore
compose.yaml
init.sql
evidencias-compose

## Uso local

docker compose up --build -d
docker compose exec -T postgres psql -U myuser -d mydb < init.sql
curl localhost:8080/api/health
curl localhost:8080/items

## Evidencias

Las capturas estan en la carpeta evidencias-compose con terminal estilo macOS.
