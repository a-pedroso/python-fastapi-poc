from fastapi import APIRouter, Depends, Query
from app.database.service import get_session
from app.database.models import Users
from app.endpoints.users.dto import UserDTO
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()

@router.get("/users/", response_model=list[UserDTO], summary="Get a list of users", description="Retrieve a list of users")
async def get(
    session: AsyncSession = Depends(get_session),
    limit: int = Query(10, description="Number of users to retrieve"),  # Default to 10 users per page
    offset: int = Query(0, description="Offset from the start of the list")  # Default to start at the first user
    ):
    query = select(Users).limit(limit).offset(offset)
    result = await session.exec(query)
    users = result.all()
    return [UserDTO(id=u.user_id, username=u.username, email=u.email) for u in users]
