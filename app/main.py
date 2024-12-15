from beanie import init_beanie, Document, UnionDoc
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from app import MONGO_DSN, projectConfig
from app.routers import user

app = FastAPI(
    title=projectConfig.__projname__,
    version=projectConfig.__version__,
    docs_url="/store/docs"
)

app.include_router(user.router)

@app.on_event('startup')
async def startup_event():
    client = AsyncIOMotorClient(MONGO_DSN)

    await init_beanie(
        database=client.get_default_database(),
        document_models=Document.__subclasses__() + UnionDoc.__subclasses__()
    )