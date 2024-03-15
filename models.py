from sqlalchemy import Column, String, Integer,Date
from sqlalchemy.orm import sessionmaker
from database import base,db_engine

class SignUp(base):
    __tablename__="user"
    id = Column(Integer, primary_key=True, index=True)
    username=Column(String(20),unique=True)
    password=Column(String(10))
    status=Column(String(20))


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


class Col(base):
    __tablename__="col"
    id=Column(Integer,primary_key=True,index=True)
    company=Column(String(20))
    status=Column(String(20))
    

base.metadata.create_all(bind=db_engine)