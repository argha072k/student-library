class MyLibrary:

    def __init__(self,BooksList):
        self.books=BooksList


    def displaybooks(self):
        print("THE BOOKS AVAILABLE IN THE LIBRARY ARE: ")
        for books in self.books:
            print(books)


    def borrowed(self,bookname):
        if bookname in self.books:
            print(f"you have borrowed {bookname} book. try to return it in 30 days***")
            self.books.remove(bookname)
            return True
        else:
            print("the book is not available currently, please wait for some days")    
            return False

    def returnbook(self,bookname):
        self.books.append(bookname)
        print("thanks for returning the book!")


class Student:
      def requestBook(self):
          self.book=input("enter the book name you want to borrow:  ")
          return self.book

      def returnbook(self):
         self.book=input("enter the book name you want to return:  ")
         return self.book


    
if __name__ == "__main__":
    centralLibrary=MyLibrary(["algorithm","python","cpp","Grammer","data science","competitive programming"])
    student1 =Student()


while(True):
    message='''------welcome to central library 
                    enter your choice:   
                    1. Display the books
                    2.I want to buy a book
                    3.I want to return the book
                    4.exit Library    '''
    print(message)  
    a=int(input("your choice:"))
    
    if a==1:
        centralLibrary.displaybooks()
    elif a==2:
        centralLibrary.borrowed(student1.requestBook())
    elif a==3:
        centralLibrary.returnbook(student1.returnbook())
    elif a==4:
        print("thanks! visit again")
        exit()         
    else:
        print("invalid choice")

       


