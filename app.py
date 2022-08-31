import time

from models import (Base, session,
                    Book, engine)
import datetime

import csv



def submenu():
    while True:
        print('''\n
      \r1) Edit
      \r2) Delete
      \r3) Return to main menu
     ''')

        choice = input('What would you like to do ?  \n')

        if choice in ['1', '2', '3']:
            return choice
        else:
            input('''\rPlease chose one of the options above.
                     \rA number from 1-3
                     \rPress enter to try again''')
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
def clean_id(id_str, options):
    try:
        book_id= int(id_str)
    except:
        input('''
                       \n****** ID EROR******
                       \rThe ID format should be a number.
                       \rPress enter to start again
                       \r******************''')
        return
    else:
        if book_id in options:
            return book_id
        else:
            input(f'''
                                   \n****** ID EROR******
                                   \rOptions: {options}
                                   \rPress enter to start again.
                                   \r******************''')
            return
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
           for book in session.query(Book):
               print(f'{book.id} | {book.title} | {book.author} | {book.published_date} | {book.price}')
           input('Press enter to return to the menu')
           pass
       elif choice == '3':
           id_options = []
           for book in session.query(Book):
               id_options.append(book.id)
           id_error = True
           while id_error:
                id_choice = input((f'''
                \n Id Options: {id_options}
                \r Book id: '''))
                id_choice = clean_id(id_choice,id_options)
                if type(id_choice)== int:
                 id_error = False
           the_book = session.query(Book).filter(Book.id==id_choice).first()
           print((f'''\n{the_book.title} by {the_book.author}
           \rPublished: {the_book.published_date}
           \rPrice: ${the_book.price/100}\n '''))
           time.sleep(1.5)
           sub_choice = submenu()
           if sub_choice=='1':

               the_book.title = edit_check('Title',the_book.title)
               the_book.author = edit_check('Author',the_book.author)
               the_book.published_date = edit_check('Published',the_book.published_date)
               the_book.price = edit_check('Price',the_book.price)
               session.commit()
               print('Book updated')
               time.sleep(1.5)



           elif sub_choice=='2':

               session.delete(the_book)
               session.commit()
               print('Book deleted')




       elif choice == '4':
           oldest_book = session.query(Book).order_by(Book.published_date).first()
           newest_book=session.query(Book).order_by(Book.published_date.desc()).first()
           total_books = session.query(Book).count()
           python_books = session.query(Book).filter(Book.title.like('%Python%')).count()
           print(f'''
           \n***** BOOK ANALYSIS *****
           \rOldest Book: {oldest_book}
           \rNewest Book: {newest_book}
           \rTotal Books: {total_books}
           \rNumber of Python Books: {python_books}''')

           input('\npress enter to continue')
       elif choice == '5':
           print('GOODBYE')
           app_running=False
           pass
def edit_check(column_name, current_value):
    print(f'\n***** Edit {column_name}*****')
    if column_name == 'Price':
        print(f'\rCurrent Value: {current_value/100}')

    elif column_name=='Date':
        print(f'\rCurrent Date: {current_value.strftime("%B %d, %Y")}')

    else:
        print(f'\rCurrent Value: {current_value}')

    if column_name == 'Date' or column_name == 'Price':
        while True:
            changes = input('What would you like to change ')
            if column_name == 'Date':
                changes = clean_date(changes)
                if type(changes) == datetime.date:
                    return changes
            elif column_name =='Price':
                changes = clean_price(changes)
                if type(changes) == int:
                    return changes
    else:
        return input('what would you like to change the value to ?')

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



