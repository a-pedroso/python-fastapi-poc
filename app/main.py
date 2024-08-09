from fastapi import FastAPI
#from app.endpoints.users import get as usersRoutes
from app.endpoints.users import map_endpoints as users_routes
import fastapi_problem_details
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="FastAPI PoC Demo", version="0.1.0")

fastapi_problem_details.init_app(app)

users_routes.register(app)

# @app.get("/")
# async def read_root():
#     return {"message": "Welcome to the API"}

app.openapi()