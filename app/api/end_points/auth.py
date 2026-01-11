

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.auth import auth
from app.db.session import get_session
from app.repositories.users import UserRepository
from app.schemas.auth import AuthRequestSchema, AuthResponseSchema
from app.services.users import UserService

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=AuthResponseSchema)
async def register(data: AuthRequestSchema, db: AsyncSession = Depends(get_session)):

    user = await UserService(db=db).register(data=data)

    token = auth.create_access_token(uid=str(user.id))

    return {"access_token": token, "token_type": "bearer"}
