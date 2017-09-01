__author__ = 'Drake'
"""
CP1404 SP52 Programming 1 - ASSIGNMENT 1
	Name: Ye Lin Htet
	ID: 13258895
	Github: https://github.com/sd4483/CP1404_Assignment1.git

	Reading list: Displays a list of books and lets the user choose either list required books, completed books, add a new book or mark a book as completed.

	Pseudocode:

	FILENAME - variable used to identify main csv file
	listoffiles - an open array created to add books later on as required, completed or marked.

	function read_file:(code from github is used)
	    file_opener = open()
	      created a variable called file_opener which opens the csv file
	    for index,data in enumerate()
	      enumerated each item in file_opener
	    data.strip
	      data is cleaned from using data.strip
	    data.split
	      data is separated by commas using data.split(",")
	    listoffiles.append
	      then all the data is added to listoffiles array using listoffiles.append(datum)
	    file_opener.close()
	      function ends here

	function main:(main function which performs all the calculations)
	    print(reading list by Ye Lin Htet, 4 books loaded from csv file)
	      A welcome message is displayed and the number of total books are displayed.
	    while valuechoice = true
	      while loop is created for the whole function to run
	    print("menu:
	    Required books
	    Completed books
	    Mark as completed
	    Add a new book
	    Quit
	    ")
	      menu has 4 choices for the user with to choose from
	    valuechoice = input("Enter your choice")
	      variable created for the user to give input
	    if valuechoice = "R" or "C" or "M" or "A" or "Q"
	      user can choose from each value which will run an if loop for that value
	    when the user chooses to quit,
	    writer=csv.writer(csvfile)
	    writer.writerows(listoffiles)
	      the code at the end writes all the listoffiles data to the books.csv and the program exits saying "good bye"

"""

from operator import itemgetter
import csv
FILENAME = "books.csv"
listoffiles = []

def read_file():
    global listoffiles
    file_opener= open(FILENAME, "r")
    for index, data in enumerate(file_opener.readlines()):
        data = data.strip()
        datum = data.split(",")
        listoffiles.append(datum)
        listoffiles.sort(key=itemgetter(1,2))
    file_opener.close()
read_file()

def main():
    print("""
    Reading list v1.0 by - Ye Lin Htet
    {} books loaded from books.csv
    """ .format(len(listoffiles)))
    valuechoice = True
    while valuechoice:

        counter = 0
        print("""
        Menu:
        (R) List Required books
        (C) List Completed books
        (A) Add new book
        (M) Mark a book as completed
        (Q) Quit
        """)
        valuechoice = input("Please enter a value \n  ")
        if valuechoice == "R" or valuechoice == "r":
            reqbook_list=[]
            print("\nRequired Books")
            for item in range(0, len(listoffiles)):
                if listoffiles[item][3] == "r":
                    reqbook_list.append(listoffiles[item])
            if len(reqbook_list) == 0:
                    print("No books required to be completed")
            else:
                for i, data in enumerate(listoffiles, 0):
                    if data[-1] == "r":
                        print(i, "-", data[0], "   by", data[1], "  ", data[2], "pages")
                        counter += 1
                total_pages = int()
                for i in listoffiles:
                    if i[-1] == "r":
                        total_pages += int(i[2])
                print("Total pages for {} books: ".format(counter), total_pages)

        elif valuechoice == "C" or valuechoice == "c":

            for i,data in enumerate(listoffiles):
                if data[-1] == "c":
                    print(i, "-", data[0], "   by", data[1], "  ", data[2], "pages")
                    counter += 1

            total_pages = int()
            for i in listoffiles:
                if i[-1] == "c":
                    total_pages += int(i[2])
            print("Total pages for {} books: " .format(counter), total_pages)

        elif valuechoice == "A" or valuechoice == "a":
            print("\n Add new book")
            book_addition = open(FILENAME, "r")

            titlesof_book= str(input("Enter Title of book"))
            while titlesof_book == "":
                print("Input cannot be blank")
                titlesof_book = str(input("Enter Title of book"))
            authorsof_book= str(input("Enter Authors name"))
            while authorsof_book == "":
                print("Input should not be blank")
                authorsof_book = str(input("Enter Authors name"))
            while True:
                try:
                    pagesof_book = int(input("Enter number of pages"))
                    if float(pagesof_book)>0:
                        break
                    else:
                        continue
                except ValueError:
                    print("Invalid input, Enter a number")
                    continue

            new_book = [titlesof_book, authorsof_book, pagesof_book, 'r']
            listoffiles.append(new_book)
            book_addition.close()

        elif valuechoice == "M" or valuechoice == "m":
            for i, data in enumerate(listoffiles, 0):
                if data [-1] == "r":
                    print(i, "-",data[0],"   by", data[1],"  ",data[2],"pages")
                    counter += 1
            total_pages = int()
            for i in listoffiles:
                if i[-1] == "r":
                    total_pages += int(i[2])
            print("Total pages for {} books: " .format(counter) , total_pages)
            print("Enter the number of the book to be marked as completed")

            while True:
                try:
                    number_identify = int(input(">>>"))
                    if number_identify < 0 or number_identify > len(listoffiles):
                        print("Invalid item number")
                    else:
                        listoffiles[number_identify][3] = "c"
                        print("{} by {} marked as completed".format(listoffiles[number_identify][0],listoffiles[number_identify][1]))
                        break
                except ValueError:
                    print("Invalid input; enter a number")


        elif valuechoice == "Q" or valuechoice == "q":
            print ("\n Good bye")
            with open(FILENAME,'w',newline="") as csvfile:
                writer=csv.writer(csvfile)
                writer.writerows(listoffiles)
            break
        else:
            print("\n Not Valid Choice Try again")


main()

