# This function reseats the book list with a default list

import save_book_file


def reset_book_list(book_list):
    book_list.clear()

    with open("books_list_default.csv", "r") as file_pointer:
        for line in file_pointer.readlines():
            line_splitted = line.strip().split(",")
            # print("line: ", repr(line))
            # print("line splitted: ", repr(line_splitted))
            book = {
                "title": line_splitted[0],
                "author(s)": line_splitted[1],
                "ISBN": line_splitted[2],
                "publishing_year": line_splitted[3],
                "price": line_splitted[4],
                "quantity": line_splitted[5],
            }
            book_list.append(book)
    save_book_file.save_books(book_list)

    return book_list


def reset_book_list_borrowed(book_list_borrowed):
    book_list_borrowed.clear()

    with open("books_list_borrowed_default.csv", "r") as file_pointer:
        for line in file_pointer.readlines():
            line_splitted = line.strip().split(",")
            # print("line: ", repr(line))
            # print("line splitted: ", repr(line_splitted))
            book = {
                "title": line_splitted[0],
                "author(s)": line_splitted[1],
                "borrower": line_splitted[2],
            }
            book_list_borrowed.append(book)

    save_book_file.save_books_borrowed(book_list_borrowed)
    return book_list_borrowed
