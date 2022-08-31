import time

from models import (Base, session,
                    Book, engine)
import datetime

import csv

def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']

    split_date = date_str.split(' ')
    try:
        month = int(months.index(split_date[0]) + 1)
        day = int(split_date[1].split(',')[0])
        year = int(split_date[2])
        return_date =datetime.date(year, month, day)
    except ValueError:
        input('''
        \n****** DATE EROR******
        \rThe date format should include a valid Month Day, Year from the past.
        \rEx: January 13, 2003
        \rPress enter to start again
        \r******************''')
        return


    return return_date


def clean_price(price_str):
    try:
        price_float = float(price_str)

    except ValueError:
        input('''
               \n****** PRICE EROR******
               \rThe price format should be a number without currency symbol.
               \rEx: 10.99
               \rPress enter to start again
               \r******************''')

    return int(price_float * 100)

def Menu():
  while True:
    print('''\nMY BOOKS
    \r1) Add book
    \r2) View all books
    \r3) Search for books
    \r4) Book analysis
    \r5) Exit''')


    choice = input('What would you like to do ?  \n')

    if choice in ['1','2','3','4','5']:
          return choice
    else:
          input('''\rPlease chose one of the options above.
                   \rA number from 1-5
                   \rPress enter to try again''')




def app():
   app_running= True
   while app_running:
       choice=Menu()

       if choice == '1':
           title=input('Title : ')
           author=input('Author : ')
           date_error=True
           while date_error:
            date=input('Published date (Ex: October 25, 2022) : ')
            date=clean_date(date)
            if type(date)== datetime.date:
                date_error=False
           price_error=True
           while price_error:
            price=input('Price (Ex: 29.99) : ')
            price=clean_price(price)
            if type(price)==int:
                price_error=False
           add_book = Book(title=title,author=author,price=price,published_date=date)
           session.add(add_book)
           session.commit()
           print('book added !')
           time.sleep(1.5)

           pass
       elif choice == '2':
           #view
           pass
       elif choice == '3':
           #search
           pass
       elif choice == '4':
           #analysis
           pass
       elif choice == '5':
           print('GOODBYE')
           app_running=False
           pass

def add_csv():
    with open('suggested_books.csv') as csvfile:

        data = csv.reader(csvfile)
        for row in data:
            title=row[0]
            author=row[1]
            date= clean_date(row[2])
            price = clean_price(row[3])

            new_book = Book(title=title,author=author,price=price,published_date=date)
            session.add(new_book)
    session.commit()


if __name__=='__main__':
    Base.metadata.create_all(engine)
    app()

    for book in session.query(Book):
        print(book)



