from app.endpoints.users import get
from app.endpoints.users import get_by_id

def register(app):
    app.include_router(get.router, prefix="/api", tags=["users"])
    app.include_router(get_by_id.router, prefix="/api", tags=["users"])