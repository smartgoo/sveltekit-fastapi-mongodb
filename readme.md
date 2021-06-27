## SvelteKit - FastAPI - MongoDB with Docker project template
This project is still in progress. Some features are incomplete or completely missing. The goal is to build this into a complete starter template for this tech stack.

- Frontend: [Svelte](https://svelte.dev/) with [SvelteKit](https://kit.svelte.dev/)
- Backend: [FastAPI](https://fastapi.tiangolo.com/)
- Database: [MongoDB](https://www.mongodb.com/)

## A big thanks to these projects
A few existing existing project templates were referenced while building this. A big thanks to these:
- [FastAPI MongoDB Real World Example](https://github.com/markqiu/fastapi-mongodb-realworld-example-app)
- [FastAPI Project Template](https://fastapi.tiangolo.com/project-generation/)
- [Jeff Astor's FastAPI Blog Posts](https://www.jeffastor.com/blog/designing-a-robust-user-model-in-a-fastapi-app) heavily influenced authentication

## A note on SvelteKit
[SvelteKit](https://kit.svelte.dev/) is in public beta (at the time of this writing on 6/20/21). Many changes (including breaking changes) are expected as the Svelte team works towards version 1.

## How to use this project template

## Features

## TODO
Misc:
- [] build a full real world app using this starter template as an example
- [] finish readme

SvelteKit
- [] environment variables
- [] deployment adaptor (including docker config to run it)

Backend
- [] Celery & Celery Beat
- [] Redis
- [] clean up FastAPI config file
- [] add user models, user crud ops, registration w/ email verification, authentication, jwt
- [] setup skeleton for permissions

Docker
- [] docker-compose.yaml and docker-compose.override.yaml
- [] add ngnix or traefik?