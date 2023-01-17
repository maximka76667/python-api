from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqlconnector://392raeo0ri7y8a1exsg1:pscale_pw_IwuSNZl2gpabQ7pC8oV1wQMySifxC3TObuw4sq8MhY0@eu-central.connect.psdb.cloud/test")

meta = MetaData()

conn = engine.connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind = engine)
Base = declarative_base()