from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from .users import create_users

users = create_users(100)

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/users")
async def users_all(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "users": users})

@app.get("/users/{user_id}")
async def user_details(request: Request, user_id: int):
    user = next((user for user in users if user["id"] == user_id), None)
    if not user:
        return {"message": "User not found"}
    return templates.TemplateResponse("user.html", {"request": request, "user": user})
