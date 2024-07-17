# save_books file after a task


def save_books(book_list):
    file_pointer = open("books_list.csv", "wt")

    with open("books_list.csv", "wt") as file_pointer:
        for book in book_list:

            line = f"{book['title']},{book['author(s)']},{book['ISBN']},{book['publishing_year']},{book['price']},{book['quantity']}\n"
            file_pointer.write(line)
            # print(line)

    file_pointer.close()


def save_books_borrowed(book_list_borrowed):
    file_pointer = open("books_list_borrowed.csv", "wt")

    with open("books_list_borrowed.csv", "wt") as file_pointer:
        for book in book_list_borrowed:

            line = f"{book['title']},{book['author(s)']},{book['borrower']}\n"
            file_pointer.write(line)
            # print(line)

    file_pointer.close()
