# flask-docker-app - Lab 6.1 Compose + PostgreSQL

Stack Flask + PostgreSQL con secrets, redes internas y volumen persistente. Imagen `flask-docker-app:2.0`, independiente del lab de Kubernetes (`flask-k8s-app:1.0`).

## Contenido

app.py
requirements.txt
Dockerfile
.dockerignore
.gitignore
.env.dev (ignorado, crear con DB_PASSWORD)
pg_password.txt (ignorado, crear con printf sin salto)
compose.yaml (Forma B, solo secret)
init.sql
evidencias-lab61/

## Uso local

printf 'devops123' > pg_password.txt
printf 'DB_PASSWORD=devops123\n' > .env.dev
docker compose up --build -d
curl localhost:8080/api/health
curl localhost:8080/items
docker compose down
docker compose up -d
curl localhost:8080/items

## Evidencias

Capturas reales en evidencias-lab61, generadas desde salidas de terminal.
