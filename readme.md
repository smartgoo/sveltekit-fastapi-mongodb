## Summary: Dockerized SvelteKit - FastAPI - MongoDB Example Project
This project is an example of how SvelteKit, FastAPI, and MongoDB can be dockerized and ran via docker compose. Note that, as of right now, this is not perfect. This project is meant to serve as an example/reference. However, it can be manually converted into a starting template. 

## UPDATED TO THE LATEST VERSIONS! 
This project was updated on October 23 2022, and uses the latest versions possible. 
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
