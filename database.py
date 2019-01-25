from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_opinion(name, title, text):
	object_opinion = Opinion(
		name = name,
		title = title,
		text = text)
	session.add(object_opinion)
	session.commit()

def get_all_opinions():
	opinions = session.query(Opinion).all()
	return opinions
    
