# Lend books

import save_book_file


def lend_book(book_list, book_list_borrowed):
    print(
        """
 =================
 ||  Lend book  ||
 =================
"""
    )
    print(" Select the book to lend by its number: \n")
    for index, book in enumerate(book_list):
        print(
            f"* {index+1}. {book['title']} | {book['author(s)']} | available copies: {book['quantity']}"
        )
        print("-")

    try:
        selected_index = int(input("\n>> Enter the book number to lend: "))
    except:
        print("\n ERROR: Please enter an integar value.")
    else:
        if 0 < selected_index < len(book_list) + 1:
            # print(type(int(book_list[selected_index - 1]["quantity"])))
            if int(book_list[selected_index-1]['quantity'])>=1:
                print(f"\n BOOK TO LEND:\n {book_list[selected_index - 1]["title"]} by {book_list[selected_index - 1]["author(s)"]}")
                
                borrower = input(" Enter borrower name: ")
                print(borrower)
                
            else:
                print("\n SORRY!\n This book has no available copies!")
            # save_book_file.save_books(book_list)
            return selected_index
        else:
            print(
                """
(#)  ================================  (#)
(#)  ||       INVALID CHOICE!      ||  (#)
(#)  ||      Returning to menu.    ||  (#)
    ================================    
(#)                                    (#)
"""
            )

    

    # title = input("* Enter book title: ")
    # author_s = input("* Enter author(s) name: ")
    # borrower = input("* Enter borrower name: ")

    # book = {
    #     "title": title,
    #     "author(s)": author_s,
    #     "borrower": borrower,
    # }

    # book_list_borrower.append(book)

    # save_book_file.save_books_borrowed(book_list_borrower)
    # print("\n Book added successfully!")
    # return book_list_borrower

def index_within_length():
    
def get_available_Book():
        