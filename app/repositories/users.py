from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import async_session
from app.models.users import User


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, name: str, email: str, hash_password: str) -> User:
        user = User(name=name, email=email, hash_password=hash_password)
        self.db.add(user)
        await self.db.flush()
        return user


    async def get_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()
