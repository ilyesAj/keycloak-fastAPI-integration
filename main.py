#/main.py
import uvicorn
from fastapi import FastAPI,Depends
from models import User
from auth import get_user_info

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/secure")
async def root(user: User = Depends(get_user_info)):
    return {"message": f"Hello {user.username} you have the following service: {user.realm_roles}"}


if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8081)