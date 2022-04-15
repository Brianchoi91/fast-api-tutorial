from email.policy import HTTP
from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

print(settings.database_username)

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


#below is to allow public access 
origins = ["*"]

#below is a list of domains that can access the api
# origins=["https://www.google.com", "https://www.youtube.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message":"hello to my API"}


