from database import (Base,session,Book, engine )
import datetime
import csv

def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']

    split_date = date_str.split(' ')
    print(split_date)
    month = int(months.index(split_date[0])+1)
    day=int(split_date[1].split(',')[0])
    year=int(split_date[2])
    return datetime.date(year, month,day)

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
           #add
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
           print('GOOD BYE')
           app_running=False
           pass

def add_csv():
    with open('suggested_books.csv') as csvfile:
        data=csv.reader(csvfile)
        for row in data:
            print(row)


if __name__=='__main__':
    Base.metadata.create_all(engine)
    #app()
    #add_csv()
    clean_date('October 24, 2017')



