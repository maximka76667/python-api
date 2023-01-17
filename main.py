from fastapi import FastAPI
from routes.index import user
app = FastAPI()

# import schemas.index
# from config.db import SessionLocal, engine
# import models.index


app.include_router(user)