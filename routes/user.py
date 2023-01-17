from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User
user = APIRouter()

@user.get("/")
async def get_users():
  return conn.execute(users.select()).fetchall()

@user.get("/{id}")
async def get_user(id: int):
  return conn.execute(users.select().where(users.c.id == id)).fetchall()

@user.post("/")
async def add_user(user: User):
  conn.execute(users.insert().values(
    name=user.name,
    email=user.email,
    password=user.password
  ))
  return conn.execute(users.select()).fetchall()

@user.put("/{id}")
async def update_user(id: int, user: User):
  conn.execute(users.update().where(users.c.id == id).values(
    name=user.name,
    email=user.email,
    password=user.password
  ))
  return conn.execute(users.select()).fetchall()

@user.delete("/{id}")
async def delete_user(id: int):
  conn.execute(users.delete().where(users.c.id == id))
  return conn.execute(users.select()).fetchall()