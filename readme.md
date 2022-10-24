## Summary: Dockerized SvelteKit - FastAPI - MongoDB Example Project
This project is an example of how SvelteKit, FastAPI, and MongoDB can be dockerized and ran via docker compose. Note that, as of right now, this is not perfect. This project is meant to serve as an example/reference. However, it can be manually converted into a starting template. 

## Getting started
1. Clone project: `git clone https://github.com/smartgoo/sveltekit-fastapi-mongodb.git`
2. `cd sveltekit-fastapi-mongodb`
3. Install SvelteKit packages: `npm install frontend/`
4. Build the containers: `docker-compose build`
5. Bring up the containers: `docker-compose up`
6. Open the web app: `http://localhost:5173/`
7. Open the FastAPI OpenAPI docs: `http://localhost:8000/docs`

## Updated To Latest Versions
This project was updated on October 23 2022, and uses the latest versions available at the time. 
- Node v16
- SvelteKit 1.0.0-next.522
- Python 3.10.8
- FastAPI 0.85.1

## Converting to a starter template
Please note this process is incomplete, but the process of converting a starter template would look roughly like this:
1. Remove FastAPI endpoints from `backend/app/api/endpoints` and update `backend/app/api/api.py` accordingly. 
2. Remove SvelteKit routes from `frontend/src/routes`.
3. Remove SvelteKit components from `frontend/src/lib`.

## Components
- Frontend: [Svelte](https://svelte.dev/) with [SvelteKit](https://kit.svelte.dev/)
- Backend: [FastAPI](https://fastapi.tiangolo.com/)
- Database: [MongoDB](https://www.mongodb.com/)

## Roadmap
I hope to add more features to this project, and convert it to a full starter template at some point. Features on the roadmap are:
1. Authentication and code to illustrate how it could work
2. Nginx with HTTPS
3. Scaffold SvelteKit (`frontend`) codebase a little bit more
4. Scaffold testing for SvelteKit and FastAPI
5. FastAPI background task examples 

## A big thanks to these projects
A few existing existing project templates were referenced while building this. A big thanks to these:
- [FastAPI MongoDB Real World Example](https://github.com/markqiu/fastapi-mongodb-realworld-example-app)
- [FastAPI Project Template](https://fastapi.tiangolo.com/project-generation/)
- [Jeff Astor's FastAPI Blog Posts](https://www.jeffastor.com/blog/designing-a-robust-user-model-in-a-fastapi-app) heavily influenced authentication
