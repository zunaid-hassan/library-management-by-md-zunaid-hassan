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
            "Title: " + book["title"],
            "Author(s): " + book["author(s)"],
            "ISBN: " + str(book["ISBN"]),
            "Publication year: " + str(book["publishing_year"]),
            "Price ($): " + str(book["price"]),
            "Quantity: " + str(book["quantity"]),
            sep=" | ",
        )
        print("-" * 106)
        number += 1
