from fastapi import FastAPI, APIRouter

from server.api.v1.users.views import router as user_router


app = FastAPI()

v1_router = APIRouter(prefix='/v1')

v1_router.include_router(user_router)

app.include_router(v1_router)
