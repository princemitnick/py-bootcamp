from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from person import Person
from user import User

user = 'root'
password = 'mysql'
host = '192.168.17.250'
port = '3306'
database = 'person'
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")


Session = sessionmaker(bind=engine)
session = Session()

#person1 = Person(1, lastname="prince", firstname="stanley")
#session.add(person1)
#session.commit()

user = User(name='John')
session.add(user)
session.commit()