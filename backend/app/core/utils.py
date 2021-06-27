from typing import Callable, Collection
from fastapi import FastAPI

from app.db.mongodb_utils import connect_to_mongo, close_mongo_connection


def create_start_app_handler(app: FastAPI) -> Callable:
    def start_app() -> None:
        connect_to_mongo(app)
    
    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    def stop_app() -> None:
        close_mongo_connection(app)
    
    return stop_app