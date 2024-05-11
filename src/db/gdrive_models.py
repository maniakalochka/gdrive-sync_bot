from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, Text, DateTime
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
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
    tg_user_id = Column(Integer, nullable=False)
    tg_file_id = Column(String, nullable=False)
    default_name = Column(String, nullable=False)  # название отправляемого файла, но не файла на диске
    upload_date = Column(DateTime, default=func.now())  
    file_size = Column(Integer, nullable=False)
    mime_type = Column(String, nullable=False) 
    folder_id = Column(String, ForeignKey('folders.folder_id'))

    def __str__(self):
        return f"Имя: {self.default_name}.{self.mime_type}[{self.file_size}]"

class GDriveFolder(Base):
    __tablename__ = 'folders'
    
    folder_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    creation_date = Column(DateTime, default=func.now())
    parent_folder_id = Column(String)


    def __str__(self):
        return f"Имя: {self.name}"



Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.commit()
session.close()