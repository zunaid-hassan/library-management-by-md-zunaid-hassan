# This function displays list of available books


def view_book_list(book_list):
    print(
        """
 =================
 ||  Book list  ||
 =================
"""
    )
    number = 1
    for book in book_list:
        print(
            " " + str(number),
            "Title: " + str(book["title"]),
            "Author(s): " + str(book["author(s)"]),
            "ISBN: " + str(book["ISBN"]),
            "Publication year: " + str(book["publishing_year"]),
            "Price ($): " + str(book["price"]),
            "Quantity: " + str(book["quantity"]),
            sep=" | ",
        )
        print("-" * 140)
        number += 1
