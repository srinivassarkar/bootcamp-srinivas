from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models import User, UserSchema

# Async engine and session
async_engine = create_async_engine('postgresql+asyncpg://user:password@localhost/dbname')
AsyncSessionLocal = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

# Async fetch users
async def fetch_users_async():
    async with AsyncSessionLocal() as session:
        users = await session.execute(User.__table__.select())
        return [UserSchema.from_orm(user) for user in users.scalars()]

if __name__ == "__main__":
    import asyncio
    users = asyncio.run(fetch_users_async())
    for user in users:
        print(user.json())