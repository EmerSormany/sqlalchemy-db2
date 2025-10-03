from sqlalchemy import create_engine
from exercicio_2 import Base

e = create_engine('sqlite:///db.db', echo=True)

Base.metadata.create_all(e)