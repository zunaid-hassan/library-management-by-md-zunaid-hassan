# This function loads the book list onto memory from storage (saved file) at the start of application


def load_book_list(book_list):

    with open("books_list.csv", "r") as file_pointer:
        for line in file_pointer.readlines():
            line_splitted = line.strip().split(",")
            book = {
                "title": line_splitted[0],
                "author(s)": line_splitted[1],
                "ISBN": line_splitted[2],
                "publishing_year": int(line_splitted[3]),
                "price": float(line_splitted[4]),
                "quantity": int(line_splitted[5]),
            }
            book_list.append(book)

    return book_list


def load_book_list_borrowed(book_list_borrowed):
    with open("books_list_borrowed.csv", "r") as file_pointer:
        for line in file_pointer.readlines():
            line_splitted = line.strip().split(",")
            book = {
                "title": line_splitted[0],
                "author(s)": line_splitted[1],
                "borrower": line_splitted[2],
            }
            book_list_borrowed.append(book)
    return book_list_borrowed
