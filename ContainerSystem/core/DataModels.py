# 数据模型

import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, Integer, String

db = SQLAlchemy()

class User(db.Model):
    @property
    def getDict(self):
        return {i.name:getattr(self,i.name) for i in self.__table__.columns}
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    username = Column(String(100),nullable=False,unique=True)
    passwordhash = Column(String(100),nullable=False)
    name = Column(String(100),nullable=True)
    info = Column(String(1000),nullable=True)
    type = Column(String(100),nullable=True)
    def getData(self):
        return {
            'id':self.id,
            'username':self.username,
            'name':self.name,
            'info':self.info,
            'type':self.type
        }

class Admin(db.Model):
    @property
    def getDict(self):
        return {i.name:getattr(self,i.name) for i in self.__table__.columns}
    __tablename__ = 'admin'
    id = Column(Integer,primary_key=True)
    admin = Column(String(100),nullable=False,unique=True)
    passwordhash = Column(String(100),nullable=False)
    name = Column(String(100),nullable=True)
    info = Column(String(1000),nullable=True)
    def getData(self):
        return {
            'id':self.id,
            'admin':self.admin,
            'name':self.name,
            'info':self.info,
        }

class Cargo(db.Model):
    @property
    def getDict(self):
        return {i.name:getattr(self,i.name) for i in self.__table__.columns}
    __tablename__ = 'cargo'
    id = Column(Integer,primary_key=True)
    cargoid = Column(String(100),nullable=False,unique=True)
    containerid = Column(String(100),nullable=False)
    title = Column(String(100),nullable=False)
    content = Column(String(1000),nullable=True)
    num = Column(Integer,nullable=False)

class Company(db.Model):
    @property
    def getDict(self):
        return {i.name:getattr(self,i.name) for i in self.__table__.columns}
    __tablename__ = 'company'
    id = Column(Integer,primary_key=True)
    companyid = Column(String(100),nullable=False,unique=True)
    name = Column(String(100),nullable=False)
    info = Column(String(1000),nullable=False,unique=True)

class Container(db.Model):
    @property
    def getDict(self):
        return {i.name:getattr(self,i.name) for i in self.__table__.columns}
    __tablename__ = 'container'
    id = Column(Integer,primary_key=True)
    containerid = Column(String(100),nullable=False,unique=True)
    companyid = Column(String(100),nullable=True)
    username = Column(String(100),nullable=False)
    title = Column(String(100),nullable=False)
    info = Column(String(1000),nullable=False)

class ContainerRegister(db.Model):
    @property
    def getDict(self):
        return {i.name:getattr(self,i.name) for i in self.__table__.columns}
    __tablename__ = 'container_register'
    id = Column(Integer,primary_key=True)
    containerid = Column(String(100),nullable=False)
    entertime = Column(DateTime,nullable=False,default=datetime.datetime.now)
    exittime = Column(DateTime,nullable=True)
    extra = Column(String(1000),nullable=True)
