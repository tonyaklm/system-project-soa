import uvicorn
from fastapi import FastAPI
from start_session import cli
from routers import users, posts

app = FastAPI()

app.include_router(users.router)
app.include_router(posts.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
    cli()
