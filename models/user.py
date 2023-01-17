from sqlalchemy import Table, Column
from sqlalchemy.types import Integer, String
from config.db import meta

users = Table(
  "users", meta, 
  Column("id", Integer, primary_key=True),
  Column("name", String(60)),
  Column("email", String(80)),
  Column("password", String(30)),
)