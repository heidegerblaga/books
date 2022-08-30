from sqlalchemy import create_engine,Column,Integer,String,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///books.db',echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column('Title',String)
    author = Column('Author',String)
    publishment = Column('Published',Date)
    status = Column('Status',String)

    def __repr__(self):
        return f'Title: {self.title} Author: {self.author} Published: {self.publishment} Status: {self.status}'


if __name__ == '__main__':
    Base.metadata.create_all(engine)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
