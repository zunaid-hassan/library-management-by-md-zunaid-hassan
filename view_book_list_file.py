# This function displays list of available books


def view_book_list(book_list):
    print(
        """
 =================
 ||  Book list  ||
 =================
"""
    )
    for book in book_list:
        print(
            "",
            "Title: " + book["title"],
            "Author(s): " + book["author(s)"],
            "ISBN: " + str(book["ISBN"]),
            "Publication year: " + str(book["publishing_year"]),
            "Price ($): " + str(book["price"]),
            "Quantity: " + str(book["quantity"]),
            sep=" | ",
        )
