from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# connect to database
###################################################################################################
SQL_ALCHEMY_DATABASE_URL = 'sqlite:///./mydb.db'
engine = create_engine(SQL_ALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False})
SessionLocal = sessionmaker(bind = engine)
Base = declarative_base() # for creating models . . .
###################################################################################################