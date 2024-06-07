import datetime
print ( 'Hello!!'.center(100))
print( 'This is your Library Managment System'.center(100))

#adding_new_books
book_list = [{'title': "Sherlock Holmes" , 'author':"Sr.arthor doyle" , 'isbn': "001" , 'status':'available'}]

def add_a_book():
     title = input ("Enter book name:")
     author = input ("Enter author name:")
     isbn = input ("Enter book ISBN:")
     books = { 'title': title , 'author':author , 'isbn': isbn , 'status':'available','time': None}
     book_list.append(books)
     print(f'"{title}"  book has been added to library' )
     

#borrow_books

def borrow():
     isbn = input ("Enter book ISBN No :")
     for book in book_list:
          if book['isbn']==isbn: 
            if book['status']=='available':
               book['status']='Borrowed'
               book ['time']= datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
               print("")
               print(f"This '{book['title']}' has been succesfully borrowed\nReading makes you perfect!!")
               return 
          print (f"Syntax Error")

#view_available_books

def availale():
           print ("Available books:")
           
           for book in book_list:
                  if book ["status"]== 'available':
                    book ['time']= datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    bookinfo = f'''
                    Title  - {book['title']}
                    Author - {book['author']}
                    ISBN   - {book['isbn']} '''  

                    print(bookinfo)
                    print("")
                    print ("Available books at '{book['time']}")
                    print('Read a book.It closes one prison...!')

#view_borrow_books

def borrow_book():
           print ("Borrowed books:")
           
           for book in book_list:
                  if book ["status"]== 'borrowed':
                    bookinfo = f'''
                    Title  - {book['title']}
                    Author - {book['author']}
                    ISBN   - {book['isbn']} '''  

                    print(bookinfo)
                  

                  
           


#return_book

def return_book():
     isbn = input ("Enter book ISBN No:")
     for book in book_list:
          if book['isbn']==isbn: 
            if book['status']=='Borrowed':
               book['status']='available'
               print("")
               print(f"This '{book['title']}' has been succesfully returned")
               print("Thank you returned this book for another one to read..!")
               return 
          print (f"Book has been not found")
    

          


def main():
      while True:
           print("")
           print("")
           print ("1.Add new book".center(100))
           print ("2.borrow new book".center(100))
           print ("3.View available books".center(100))
           print ("4.View borrow books".center(100))
           print ("5.Return book".center(100))
           print ("6.Quit the system".center(100))
     
           select = input ( "Enter your Command:")
           if select == "1":
                add_a_book()
           elif select == "2":
                borrow()
           elif select == "3":
                availale()
           elif select == "4":
                borrow_book()
           elif select == "5":
                return_book()
           elif select == "6":
                print("")
                print ('Leaving the system.Have a great day!')
                break 
           
main()
