# This function returns a borrowed book to the library


def return_book(book_list, book_list_borrowed):
    print(
        """
 ===================
 ||  Return book  ||
 ===================
"""
    )
    display_book_list_borrowed(book_list_borrowed)
    selected_index = get_book_index()
    if is_index_within_length(book_list_borrowed, selected_index) == True:
        title = get_book_title(book_list_borrowed, selected_index)
        borrower = get_borrower(book_list_borrowed, selected_index)
        book_list_borrowed = remove_book_borrowed_entry(
            book_list_borrowed, selected_index
        )
        book_list = increase_book_quantity(book_list, title)
        print("\n", title, "has been returned successfully by", borrower + "!")
        return book_list, book_list_borrowed
    else:
        print("Sorry, selection out of range!")


def display_book_list_borrowed(book_list_borrowed):
    print(" Select the book to return by its number: \n")
    for index, book in enumerate(book_list_borrowed):
        print(
            f"* {index+1}. {book['title']} | {book['author(s)']} | borrowed by: {book['borrower']}"
        )
        print("-" * 60)


def get_book_index():
    try:
        selected_index = int(input("\n>> Enter the book number to return: "))
    except:
        print("\n ERROR: Please enter an integar value.")
    else:
        return selected_index


def is_index_within_length(book_list_borrowed, selected_index):
    if 0 < selected_index < len(book_list_borrowed) + 1:
        return True
    else:
        return False


def get_book_title(book_list_borrowed, selected_index):
    title = book_list_borrowed[selected_index - 1]["title"]
    return title


def get_borrower(book_list_borrowed, selected_index):
    borrower = book_list_borrowed[selected_index - 1]["borrower"]
    return borrower


def remove_book_borrowed_entry(book_list_borrowed, selected_index):
    book_list_borrowed.pop(selected_index - 1)


def increase_book_quantity(book_list, title):
    for book in book_list:
        if book["title"] == title:
            book["quantity"] += 1
            return book
        else:
            continue
    return book
