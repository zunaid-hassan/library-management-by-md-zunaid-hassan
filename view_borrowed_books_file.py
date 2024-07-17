# This function displays list of borrowd books


def view_borrowed_book_list(book_list_borrowed):
    print(
        """
 ==========================
 ||  Borrowed book list  ||
 ==========================
"""
    )
    for book in book_list_borrowed:
        print(
            "",
            "Title: " + book["title"],
            "Author(s): " + book["author(s)"],
            "Borrowed by: " + book["borrower"],
            sep=" | ",
        )
