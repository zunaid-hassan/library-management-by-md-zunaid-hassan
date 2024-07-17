# This function removes selected book

import save_book_file


def remove_book(book_list):
    found_search_result = False
    search_term = str(input("\n>> SEARCH for title(s) to remove: "))
    for index, book in enumerate(book_list):
        if search_term.lower() in book["title"].lower():
            found_search_result = True
            print(f"* {index+1}. {book['title']} - {book['author(s)']}")

    if not found_search_result:
        print(
            """
 ==================== 
 || NO ITEM FOUND! ||
 ====================
"""
        )
        return

    try:
        selected_index = int(input("\n>> Enter a book to remove: "))
    except:
        print("\n ERROR: Please enter an integar value.")
    else:
        if 0 < selected_index < len(book_list) + 1:
            print(f"\n Book removed successfully:\n * {book_list[selected_index - 1]["title"]} by {book_list[selected_index - 1]["author(s)"]}")
            book_list.pop(selected_index - 1)          
            return book_list
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
    return book_list
    save_book_file.save_books(book_list)
    return book_list
