from fastapi import FastAPI

from models.config import settings
from routes.user import router as user_router
from routes.token import router as token_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

app.include_router(
    router=user_router,
    prefix='/user',
    tags=['User']
)

app.include_router(
    router=token_router,
    prefix='/token',
    tags=['Token']
)


@app.get("/")
async def hello_world():
    return {"msg": "Hello World"}
