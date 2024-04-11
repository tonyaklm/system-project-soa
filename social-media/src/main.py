import uvicorn
from fastapi import FastAPI
from routers import users, posts
from fastapi_pagination import add_pagination

app = FastAPI()

app.include_router(users.router)
app.include_router(posts.router)

add_pagination(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
