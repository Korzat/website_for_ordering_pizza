from fastapi import FastAPI
from app.api.end_points.auth import router as auth_router
from app.core.auth import auth

app = FastAPI()




auth.handle_errors(app)

app.include_router(auth_router)