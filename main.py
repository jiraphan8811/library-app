from Library import *
import justpy as jp



def main():            
      library=Library(["The Last Battle","The Screwtape letters","The Great Divorce"])
      student=Student()
      done=False
      while done==False:
            print(""" ======LIBRARY MENU=======
                  1. Display all available books
                  2. Request a book
                  3. Return a book
                  4. Exit
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                        library.displayAvailablebooks()
            elif choice==2:
                        library.lendBook(student.requestBook())
            elif choice==3:
                        library.addBook(student.returnBook())
            elif choice==4:
                  sys.exit()

                  
                  
def hello_world():
    wp = jp.WebPage()
    p = jp.P(text='Hello World!', a=wp)
    return wp

jp.justpy(hello_world)