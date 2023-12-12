import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column (Integer, primary_key=True)
    name = Column (String(250), nullable=False)
    user_name= Column (String(30), nullable=False)
    email= Column (String(100), nullable=False)
    password= Column (String(100), nullable=False)
    registration_date= Column (Integer, nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id_post = Column (Integer, primary_key=True)
    creation_date = Column (Integer)
    like_post = Column (Integer)
    user_id= Column (Integer, ForeignKey ('user.id'))
    user = relationship ('user.id')

class Video(Base):
    __tablename__= 'video'
    id_reels_= Column (Integer, primary_key=True)
    reproductions = Column(Integer)
    likes = Column (Integer)
    comments= Column (Integer)
    times_it_has_been_saved= Column (Integer)
    times_it_has_been_shared= Column (Integer)
    hashtags_used= Column (Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Reel(Base):
    __tablename__= 'reel'
    id_reel = Column (Integer, primary_key=True)
    reproductions =  Column (Integer)
    likes = Column (Integer)
    comments = Column (Integer)
    times_it_has_been_saved = Column(Integer)
    times_it_has_been_shared = Column(Integer)
    hashtags_used = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)   

class Photo(Base):
    __tablename__= 'photo'
    id_photo = Column (Integer, primary_key=True)
    impressions = Column (Integer) 
    likes = Column (Integer)
    comments = Column (Integer)
    times_it_has_been_saved = Column (Integer)
    times_it_has_been_shared = Column (Integer)
    hashtags_used = Column (Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User) 

class Followers (Base):
    __tablename__ = 'followers'
    followers = Column (Integer, primary_key=True)
    followed = Column (Integer)
    direct_messages = Column (Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
