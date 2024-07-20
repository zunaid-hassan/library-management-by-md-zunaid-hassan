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
    display_book_list(book_list)
    
    selected_index = get_book_index()
    borrower = ""
    
    if is_index_within_length(book_list, selected_index) == True:
        check_if_available(book_list, selected_index)
        if check_if_available(book_list, selected_index) == True:
            print(f"\n BOOK TO LEND:\n {book_list[selected_index - 1]["title"]} by {book_list[selected_index - 1]["author(s)"]}")
            borrower = get_borrower_name()
            reduce_book_quantity(book_list, selected_index)
            add_book_to_borrowed_list(book_list, selected_index, book_list_borrowed, borrower)            
            return book_list, book_list_borrowed
        else:
            print("\n SORRY!\n This book has no available copies!")
    else:
        print("""
(#)  ================================  (#)
(#)  ||       INVALID CHOICE!      ||  (#)
(#)  ||      Returning to menu.    ||  (#)
     ================================    
(#)                                    (#)
""")
        
    return book_list, book_list_borrowed
    




def display_book_list(book_list):
    print(" Select the book to lend by its number: \n")
    for index, book in enumerate(book_list):
        print(
            f"* {index+1}. {book['title']} | {book['author(s)']} | available copies: {book['quantity']}"
        )
        print("-"*60)

def get_book_index():
    try:
        selected_index = int(input("\n>> Enter the book number to lend: "))
    except:
        print("\n ERROR: Please enter an integar value.")
    else:
        return selected_index

def is_index_within_length(book_list, selected_index):
    if 0 < selected_index < len(book_list) + 1:
        return True
    else:        
        return False

def check_if_available(book_list, selected_index):
    if int(book_list[selected_index-1]['quantity'])>=1:    
        return True        
    else:
        return False
    

def get_borrower_name():        
    borrower = input("\n>> Enter borrower name: ")
    return borrower

def reduce_book_quantity(book_list, selected_index):
    (book_list[selected_index-1]['quantity'])=int((book_list[selected_index-1]['quantity']))-1
    return book_list

def add_book_to_borrowed_list(book_list, selected_index, book_list_borrowed, borrower):
    title = book_list[selected_index - 1]['title']
    author_s = book_list[selected_index - 1]['author(s)']
    borrowed_book = {
        "title" : title,
        "author(s)" : author_s,
        "borrower" : borrower,
    }
    print("\n",book_list[selected_index-1]['title'],"lent to", borrower, "successfully!")
    book_list_borrowed.append(borrowed_book)     
        
