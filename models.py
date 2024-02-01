from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from database import base,db_engine

class SignUp(base):
    __tablename__="user"
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String(20))
    regno=Column(Integer)
    email=Column(String(30))
    genter=Column(String(5))
    number=Column(Integer)
    year=Column(String(10))
    department=Column(String(10))
    degree=Column(String(20))
    area=Column(String(20))
    status=Column(String(10))

class New(base):
    __tablename__="rev"
    id=Column(Integer,primary_key=True,index=True)
    ename=Column(String(20))
    session=Column(String(20))
    logindate=Column(String(20))
    logintime=Column(String(20))
    logouttime=Column(String(20))
    status=Column(String(10))

class Card(base):
    __tablename__="card"
    id=Column(Integer,primary_key=True,index=True)
    cname=Column(String(10))
    overview=Column(String(30))
    cgpa=Column(String(20))
    twelfth=Column(String(20))
    tenth=Column(String(20))
    ddate=Column(String(20))
    jdetails=Column(String(20))
    Description=Column(String(255))
    contact=Column(String(20))

base.metadata.create_all(bind=db_engine)