
# app/core/auth.py
from authx import AuthX, AuthXConfig
from app.core.config import settings

config = AuthXConfig(
    JWT_SECRET_KEY=settings.JWT_SECRET_KEY,
    JWT_TOKEN_LOCATION=["headers"],
)
auth = AuthX(config=config)
