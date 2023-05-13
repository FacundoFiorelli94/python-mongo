from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="REST API - FastAPI and MongoDB CRUD",
)

app.include_router(user)

