# This function searches the book list by author

def search_books_author(book_list):
    
    found_search_result = False
    
    print("""
 ====================================
 ||       Search by author(s)      ||  
 ====================================
""")
    search_term = str(input("\n>> Enter author name: "))
    
    for book in book_list:
        if search_term.lower() in book["author(s)"].lower():
            print("""
 ========================
 ||    Found books     ||  
 ========================
""")
            break
        
    for book in book_list:
        if search_term.lower() in book["author(s)"].lower() :
            found_search_result = True
            print(f"* Found: {book["title"]} by {book["author(s)"]}")
            
    if not found_search_result:
        print("""
 ==================== 
 || NO ITEM FOUND! ||
 ====================
              """)
        return
