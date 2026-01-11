from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import hash_password
from app.models.users import User
from app.repositories.users import UserRepository
from app.schemas.users import UserCreateSchema


class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repo = UserRepository(db)


    async def register(self, data: UserCreateSchema) -> User:

        existing_user = await self.repo.get_by_email(data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='User with this email already exists'
            )

        hashed_password = hash_password(data.not_hash_password)

        user = await self.repo.create(name=data.name, email=data.email, hash_password=hashed_password)

        await self.db.commit()
        await self.db.refresh(user)
        return user

