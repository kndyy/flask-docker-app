# lab-docker-flask

Aplicacion Flask contenida con Docker para el laboratorio 5.1.

## Contenido

app.py
requirements.txt
Dockerfile
Dockerfile.alpine
.dockerignore
evidencias

## Uso local

docker build -t flask-docker-app:1.0 .
docker run -d -p 8080:5000 --name mi-flask-app flask-docker-app:1.0
curl http://localhost:8080/api/health
curl http://localhost:8080/api/info

## Docker Hub

leonardocandio/flask-docker-app:1.0
leonardocandio/flask-docker-app:latest

## Reto

Base slim: python:3.11-slim, imagen 149MB
Base alpine: python:3.11-alpine, imagen 77.1MB
Alpine es mas liviana porque trae menos paquetes del sistema.

## Evidencias

Las capturas estan en la carpeta evidencias con terminal estilo macOS.
