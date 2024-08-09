from fastapi import APIRouter

router = APIRouter()

@router.get("/users/{id}")
async def get_by_id(id: int):
    return {"user_id": id}
