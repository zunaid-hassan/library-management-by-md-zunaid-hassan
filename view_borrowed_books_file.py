# This function displays list of borrowd books


def view_borrowed_book_list(book_list_borrowed):
    print(
        """
 ==========================
 ||  Borrowed book list  ||
 ==========================
"""
    )
    number = 1
    for book in book_list_borrowed:
        print(
            " " + str(number),
            "Title: " + book["title"],
            "Author(s): " + book["author(s)"],
            "Borrowed by: " + book["borrower"],
            sep=" | ",
        )
        print("-" * 78)
        number += 1
