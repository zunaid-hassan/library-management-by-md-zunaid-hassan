# This function allows user to add book

import save_book_file


def add_book(book_list):
    print(
        """
 =================
 ||  Add book   ||
 =================
"""
    )
    title = input("* Enter book title: ")
    author_s = input("* Enter author(s) name: ")
    ISBN = input("* Enter ISBN number: ")
    publishing_year = int(input("* Enter publication year: "))
    price = float(input("* Enter price ($): "))
    quantity = int(input("* Enter quantity: "))

    book = {
        "title": title,
        "author(s)": author_s,
        "ISBN": ISBN,
        "publishing_year": publishing_year,
        "price": price,
        "quantity": quantity,
    }

    book_list.append(book)

    save_book_file.save_books(book_list)
    print("\n Book added successfully!")
    return book_list
