from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from laddr.db import engine
from laddr.contacts import models
from laddr.contacts.routes import contacts as contact_router

models.Base.metadata.create_all(bind=engine)


def create_app():
    app = FastAPI()
    origins = ["http://localhost", "http://localhost:3000"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/")
    async def index():
        return {"hello": "world"}

    app.include_router(contact_router, tags=["contacts"], prefix="/contacts")

    return app
