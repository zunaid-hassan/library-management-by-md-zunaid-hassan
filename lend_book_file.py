# Lend books

import save_book_file


def lend_book(book_list_borrower):
    print(
        """
 =================
 ||  Lend book  ||
 =================
"""
    )
    title = input("* Enter book title: ")
    author_s = input("* Enter author(s) name: ")
    borrower = input("* Enter borrower name: ")

    book = {
        "title": title,
        "author(s)": author_s,
        "borrower": borrower,
    }

    book_list_borrower.append(book)

    save_book_file.save_books_borrowed(book_list_borrower)
    print("\n Book added successfully!")
    return book_list_borrower
