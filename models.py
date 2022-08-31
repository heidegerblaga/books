from sqlalchemy import (create_engine,Column,
                        Integer,String,Date)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///books2.db',echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column('Title',String)
    author = Column('Author',String)
    published_date = Column('Published', Date)
    price = Column('Price',Integer)


    def __repr__(self):
        return f'Title: {self.title} Author: {self.author} Published: {self.published_date} Price: {self.price}'


if __name__ == '__main__':
    Base.metadata.create_all(engine)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
