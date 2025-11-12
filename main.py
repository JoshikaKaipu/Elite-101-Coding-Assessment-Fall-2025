from library_books import library_books as library_books
from datetime import datetime, timedelta, date

class Book:
    def __init__(self, id, title, author, genre, available, due_date, checkouts):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts


bookList = []

for aBook in library_books:
    book = Book(aBook['id'], aBook['title'], aBook['author'], aBook['genre'], aBook['available'], aBook['due_date'], aBook['checkouts'])
    bookList.append(book)


class Options:
    # -------- Level 1 --------
    # TODO: Create a function to view all books that are currently available
    # Output should include book ID, title, and author
    def getBooks():
        print("The books available are: ")
        for book in bookList:
            print()
            print(f"Book: {book.id}")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
        
        print()



    # -------- Level 2 --------
    # TODO: Create a function to search books by author OR genre
    # Search should be case-insensitive
    # Return a list of matching books

    def searchBook():
        searchWord = input("What author or genre are you looking for? ").lower()
        booksFound = False
        if searchWord != "":
            print()
            print("Search Results: ")
            for book in bookList:
                if (searchWord in (book.author).lower()) or (searchWord in (book.genre).lower()):
                    print()
                    print(f"Book: {book.id}")
                    print(f"Title: {book.title}")
                    print(f"Author: {book.author}")
                    booksFound = True
            if booksFound == False:
                print(f"Sorry, no books were found matching {searchWord}")
            print()
        else:
            print("Sorry, please enter a valid input next time!")



    # -------- Level 3 --------
    # TODO: Create a function to checkout a book by ID
    # If the book is available:
    #   - Mark it unavailable
    #   - Set the due_date to 2 weeks from today
    #   - Increment the checkouts counter
    # If it is not available:
    #   - Print a message saying it's already checked out

    def checkOut():
        bookChoice = input("What is the ID of the book you would like to check out? ").lower()
        available = False
        checkOutBook = ""
        newDate = ''
        printed = False
        if bookChoice != "":
            for book in bookList:
                if (bookChoice == (book.id).lower()):
                    checkOutBook = book.title
                    print()
                    if book.available == True:
                        print(f"Yes, we have {checkOutBook}!")
                        book.available = False
                        todayDate = date.today()
                        newDate = todayDate + timedelta(days = 14)
                        book.due_date = newDate.strftime("%Y-%m-%d")
                        book.checkouts = book.checkouts + 1
                        print(f"The book will be due on {newDate}")
                        available = True
                        printed = True
                    break
        else:
            print("Sorry, please enter a valid input next time.")
            printed = True
        
        if printed != True:
            if available == False and checkOutBook != "":
                print(f"Sorry, we don't have {checkOutBook} as it has already been checked out.")
            else:
                print("Sorry, we don't have a book with that id.")

        print()
        
    #checkOut()

    # -------- Level 4 --------
    # TODO: Create a function to return a book by ID
    # Set its availability to True and clear the due_date

    def returnBook():
        bookID = input("What is the ID of the book? ").lower()
        fixed = False
        if bookID != "":
            for book in bookList:
                if (bookID == (book.id).lower()):
                    book.available = True
                    book.due_date = None
                    fixed = True
                    print(f"{book.title} had been successfully returned!")
                    break
            
            if fixed == False:
                print("Sorry, we don't have a book by that ID.")
        else:
            print("Sorry, please enter a valid input next time!")

        print()



    # TODO: Create a function to list all overdue books
    # A book is overdue if its due_date is before today AND it is still checked out

    def viewOverdue():
        fixed = False
        print()
        count = 0
        count2 = 0
        for book in bookList:
            if (book.due_date != None):
                bookDate = datetime.strptime(book.due_date, "%Y-%m-%d").date()
                if (bookDate < date.today()) and (book.available == False):
                    if count<1:
                        print("The books overdue are: ")
                    print()
                    print(book.id)
                    print(book.title)
                    print(book.author)
                    print(book.genre)
                    print(f"It was due on {bookDate}")
                    fixed = True
                    count+=1
                    continue
                if (bookDate == date.today()) and (book.available == False):
                    print()
                    print()
                    if count2<1:
                        print("You have a book due today!")
                    print(book.id)
                    print(book.title)
                    print(book.author)
                    print(book.genre)
                    print()
                    fixed = True
                    count2+=1
                    continue
        if fixed == False:
            print("You have no overdue books!")

    #viewOverdue()

    def viewTopThree():
        countList = []
        for book in bookList:
            countList.append(book.checkouts)
        
        finalBookList = []
        finalCountList = []
        countList.sort(reverse=True)
        for i in range(len(bookList)):
            for book in bookList:
                if (countList[i] == book.checkouts) and (book.title not in finalBookList):
                    finalBookList.append(book.title)
                    finalCountList.append(book.checkouts)
                    break

        topOneB = finalBookList[0]
        topTwoB = finalBookList[1]
        topThreeB = finalBookList[2]

        print()
        print("The top 3 books are: ")
        print()
        print(f"1. {topOneB} with {finalCountList[0]} checkouts.")
        print(f"2. {topTwoB} with {finalCountList[1]} checkouts.")
        print(f"3. {topThreeB} with {finalCountList[2]} checkouts.")


    # -------- Level 5 --------
    # TODO: Convert your data into a Book class with methods like checkout() and return_book()
    # TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

    # -------- Optional Advanced Features --------
    # You can implement these to move into Tier 4:
    # - Add a new book (via input) to the catalog
    # - Sort and display the top 3 most checked-out books
    # - Partial title/author search
    # - Save/load catalog to file (CSV or JSON)
    # - Anything else you want to build on top of the system!

    if __name__ == "__main__":
        # You can use this space to test your functions
        pass




def runLibrary():
    print("Welcome to the library!")
    while (True):
        print("1. View Available Books")
        print("2. Search")
        print("3. Checkout")
        print("4. Return a Book")
        print("5. View Overdue Books")
        print("6. View Top 3 Most Checked Out Books ")
        print("7. Exit")
        print()
        userChoice = input("Please enter your choice: ")

        if userChoice == "1":
            Options.getBooks()
            print()
        elif userChoice == "2":
            Options.searchBook()
            print()
        elif userChoice == "3":
            Options.checkOut()
            print()
        elif userChoice == "4":
            Options.returnBook()
            print()
        elif userChoice == "5":
            Options.viewOverdue()
            print()
        elif userChoice == "6":
            Options.viewTopThree()
            print()
        elif userChoice == "7":
            print("Thanks for visiting the online library!")
            print()
            break
        else:
            print("Please try again and enter with a valid input.")
            print()

runLibrary()


'''
1. Write all the functions
2. Code placeholders in each function that give the overall function
3. Work on each function
4. Continue for all the functions
5. Group them into a file that calls them at the user's request
6. Run and test the code between each new function and check if it works

Function One:

Level One:
Write a function that prints the dictionary of books available
Print them in a way that is easy to read
Use a for loop to loop through the dictionary
'''

'''
Move on to the 'Solve' phase of UCASE by implementing your Level 1 solution.
Use your pseudocode and planning from the previous section as a guide.
Focus: list all available books (print ID, title, author).
Test your code using library_books from library_books.py.
Guidelines:

Write clear and concise code. Keep your functions well-structured and easy to read. (e.g., get_available_books(data) and print_available_books(books)).
Use comments to explain your logic. Clearly describe what each function does.
Debug systematically. If you encounter issues, check your logic and review each step
Tips:

Start Simple: Begin by writing a function that lists all available books (ID, title, author).
Iterate Through Data: Loop through the library_books list and check each book’s available status
Testing: Test your code at each step.

'''

'''
Sources:
https://docs.python.org/3/howto/sorting.html  Python Documentation for sorting numbers: Used for the optional advanced 
feature of finding the top three checkouts

'''