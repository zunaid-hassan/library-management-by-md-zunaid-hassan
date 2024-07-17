# This function searches the book list by title or ISBN number

def search_books_title_isbn(book_list):
    
    found_search_result = False
    
    print("""
 ====================================
 ||    Search by title or ISBN     ||  
 ====================================
""")
    search_term = input("\n>> Enter title name or ISBN number: ")
    
    for book in book_list:
        if search_term.lower() in book["title"].lower() or search_term in book["ISBN"]:
            print("""
 ========================
 ||    Found books     ||  
 ========================
""")
            break
        
    for book in book_list:
        if search_term.lower() in book["title"].lower() or search_term in book["ISBN"]:
            found_search_result = True
            print(f"* Found: {book["title"]} by {book["author(s)"]}, ISBN: {book["ISBN"]}")
            
    if not found_search_result:
        print("""
 ==================== 
 || NO ITEM FOUND! ||
 ====================
              """)
        return
