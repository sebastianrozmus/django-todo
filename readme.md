Projekt zaliczeniowy z przedmioty Tworzenie usług sieciowych

Odpalanie projektu:
===================

 > docker-compose up -d --build

Openapi:
========

backend/openapi.yml


Autoryzacja:
============

curl --request POST \
  --url http://localhost:8000/rest-auth/login/ \
  --header 'Content-Type: application/json' \
  --data '{"password": "todo","username": "todo"}'

Tworzenie kategorii:
====================

curl --request POST \
  --url http://localhost:8000/category/ \
  --header 'Authorization: Token {TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{"name": "test"}'

Lista Kategorii:
================

curl --request GET \
  --url http://localhost:8000/category/ \
  --header 'Authorization: Token {TOKEN}' \

Lista zadań:
============

curl --request GET \
  --url http://localhost:8000/todo/ \
  --header 'Authorization: Token {TOKEN}' \

Pobieranie zadania:
===================

curl --request GET \
  --url http://localhost:8000/todo/6 \
  --header 'Authorization: Token {TOKEN}' \


Dodawanie zadania:
==================

curl --request POST \
  --url http://localhost:8000/todo/ \
  --header 'Authorization: Token {TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{"title": "test", "category": 1, "content": "123"}'

Akceptowanie zadania:
=====================

curl --request PUT \
  --url http://localhost:8000/todo/18/ \
  --header 'Authorization: Token {TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{"is_complete": true}'