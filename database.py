from model import *
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def touch(filename):
	if not os.path.exists(filename):
		return
	try:
		os.utime(filename, None)
	except OSError:
		open(filename, 'a').close()

def create_opinion(name, title, text):
	object_opinion = Opinion(
		name = name,
		title = title,
		text = text)
	session.add(object_opinion)
	session.commit()

def get_id(name, title, text):
	op_object = session.query(Opinion).filter_by(name=name, title=title, text=text).first()
	return op_object.id

def change_url(identity, img_url):
	op_object = session.query(Opinion).filter_by(id=identity).first()
	op_object.image_url = img_url
	session.commit()

def get_all_opinions():
	opinions = session.query(Opinion).all()
	return opinions
    
