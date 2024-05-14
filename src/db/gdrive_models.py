from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, Text, DateTime
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.sql import func
from dotenv import load_dotenv
import os


load_dotenv()
USER = os.getenv('USER')
PASSWORD= os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DB_NAME = os.getenv('DB_NAME')


engine = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}/{DB_NAME}', echo=True)  

Base = declarative_base()

class File(Base):
    __tablename__ = 'files'
    
    id = Column(Integer, primary_key=True)  # локальный для БД, создается при отправке на диск
    gdrive_id = Column(String, nullable=False)  # id, который дает диск
    default_name = Column(String, nullable=False) 
    upload_date = Column(DateTime, default=func.now())  
    file_size = Column(Integer, nullable=True)
    mime_type = Column(String, nullable=True) 

    def __str__(self):
        return f"Имя: {self.default_name}.{self.mime_type}[{self.file_size}]"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.commit()
session.close()