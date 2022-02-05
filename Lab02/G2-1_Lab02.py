class Book:
    def __init__(self, isbn, author, title, subject, dds_number):
        self._isbn = isbn
        self.author = author
        self.title = title
        self.subject = subject
        self.dds_number = dds_number

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, new_isbn):
        if isinstance(new_isbn, str) and new_isbn.isdecimal():
            self._isbn = new_isbn
        else:
            print("Please enter a valid isbn.")


class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print("Please enter a valid name")


class Catalog:
    def __init__(self):
        self.book = []

    def search_book(self):
        search_result = []
        print("===== Search Book =====")
        print("Select 1 : Search from Title")
        print("Select 2 : Search from ISBN")
        print("Select 3 : Search from DSS Number")
        print("Select 4 : Search from Author")
        print("Select 0 : Exit")
        print("===================================")
        while 1:
            chk = False
            search_select = str(input("Please Select : "))
            for i in range(0, 5):
                if search_select == str(i):
                    chk = True
            if chk:
                break
        while 1:
            keyword = str(input("Please Enter Keyword or * for Search all Book  : "))
            if keyword != "":
                break
        check_count = 0
        for i in range(len(self.book)):
            if keyword == "*":
                search_result.append(self.book[i])
                check_count += 1
            elif search_select == "1" and keyword.lower() in str(self.book[i].title).lower():
                search_result.append(self.book[i])
                check_count += 1
            elif search_select == "2" and keyword.lower() in str(self.book[i].isbn).lower():
                search_result.append(self.book[i])
                check_count += 1
            elif search_select == "3" and keyword.lower() in str(self.book[i].dds_number).lower():
                search_result.append(self.book[i])
                check_count += 1
            elif search_select == "4":
                for ii in range(len(self.book[i].author)):
                    if keyword.lower() in str(self.book[i].author[ii]).lower():
                        search_result.append(self.book[i])
                        check_count += 1
        if check_count == 0:
            print("===================================")
            print("Book not Found")
            print("===================================")
        else:
            for i in range(len(search_result)):
                txt_author = ""
                print("===== Book " + str(i + 1) + " =====")
                print("ISBN : " + str(search_result[i].isbn))
                for ii in range(len(search_result[i].author)):
                    if ii > 0:
                        txt_author += ", " + str(search_result[i].author[ii].name)
                    else:
                        txt_author += str(search_result[i].author[ii].name)
                print("Author : " + txt_author)
                print("Title : " + str(search_result[i].title))
                print("Subject : " + str(search_result[i].subject))
                print("DDS Number : " + str(search_result[i].dds_number))
                print("===================")

    def add_book(self):
        print("===== Add Book =====")

        # Check Duplicate ISBN
        while 1:
            isbn = str(input("Enter ISBN : "))
            chk_duplicate = False
            chk_isbn = False
            if isinstance(isbn, str) and isbn.isdecimal() and isbn != "":
                chk_isbn = True
            else:
                print("Please enter a valid ISBN")
            if chk_isbn:
                for i in range(len(self.book)):
                    if isbn == self.book[i].isbn:
                        chk_duplicate = True
                if chk_duplicate:
                    print("ISBN Duplicate Please Enter ISBN again")
                else:
                    break

        while 1:
            author = input("Enter Author : ")
            author_split = author.split(sep=", ")
            author_split_ = []
            author_split__ = []
            chk_author = 0
            for i in range(len(author_split)):
                author_split_.extend(author_split[i].split(sep=" "))
            for i in range(len(author_split_)):
                author_split__.extend(author_split_[i].split(sep="-"))
            for i in range(len(author_split__)):
                if isinstance(author_split__[i], str) and author_split__[i].isalpha():
                    chk_author += 1
            if author != "" and chk_author == len(author_split__):
                break
            else:
                print("Please enter a valid Author")

        while 1:
            title = input("Enter Title : ")
            if title != "":
                break

        while 1:
            subject = input("Enter Subject : ")
            if subject != "":
                break

        while 1:
            dds_number = input("Enter DDS Number : ")
            chk_dds_number = False
            if isinstance(isbn, str) and dds_number.isdecimal():
                chk_dds_number = True
            else:
                print("Please enter a valid DSS Number")
            if dds_number != "" and chk_dds_number:
                break

        author_split = author.split(sep=", ")
        author_list = []

        # Check duplicate Author and Add new Author
        for i in range(len(author_split)):
            author_list.append(Author(author_split[i]))

        new_book = Book(isbn, author_list, title, subject, dds_number)
        self.book.append(new_book)
        print("===================================")
        print("Add Book "+str(new_book.isbn)+" "+str(new_book.title)+" Complete")
        print("===================================")

    def delete_book(self):
        print("===== Delete Book =====")
        while 1:
            isbn = input("Enter ISBN : ")
            if isbn != "":
                break
        # Check ISBN
        chk_del = False
        for i in range(len(self.book)):
            if isbn == self.book[i].isbn:
                print("===================================")
                print("Delete Book "+str(self.book[i].isbn)+" "+str(self.book[i].title)+" Complete")
                print("===================================")
                del self.book[i]
                chk_del = True
                break
        if not chk_del:
            print("===================================")
            print("Book not Found")
            print("===================================")


catalog = Catalog()

author1 = Author("Anuwat")
author2 = Author("Supamit")

catalog.book.append(Book("1231231231231", [author1], "Code with Anuwat", "Python", "1122333"))
catalog.book.append(Book("3213213213213", [author2], "Sleep at Supamit", "Chill", "3322111"))


while 1:
    print("===== Welcome to Book Catalog =====")
    print("Select 1 : Add Book")
    print("Select 2 : Delete Book")
    print("Select 3 : Search Book")
    print("Select 0 : Exit")
    print("===================================")
    select = str(input("Please Select : "))

    if select == "0":
        break
    elif select == "1":
        catalog.add_book()
    elif select == "2":
        catalog.delete_book()
    elif select == "3":
        catalog.search_book()
