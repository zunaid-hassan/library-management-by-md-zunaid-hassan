# Ostad Full Stack Web Development with Python, Django & React
# Assignment 2 - Library Management System
# Prepared by - Md Zunaid Hassan | zunaid.hassan.t@gmail.com | 01827401503

# Import necessary function files
import view_book_list_file
import view_borrowed_books_file
import search_books_title_isbn_file
import search_books_author_file
import add_book_file
import remove_book_file
import lend_book_file
import return_book_file
import reset_system_file
import load_book_list_file
import messages_file
import save_book_file

book_list = [
    # {
    #     "title": "Harry Potter 1",
    #     "author(s)": "J. K. Rowling",
    #     "ISBN": "1338878921",
    #     "publishing_year": "1998",
    #     "price": 15.00,
    #     "quantity": 5,
    # },
    # {
    #     "title": "Harry Potter 2",
    #     "author(s)": "J. K. Rowling",
    #     "ISBN": "4390648742",
    #     "publishing_year": "2000",
    #     "price": 16.00,
    #     "quantity": 2,
    # },
]

book_list_borrowed = [
    #     {"title": "Himu 1", "borrower": "Ostad"},
    #     {"title": "Himu 2", "borrower": "Sumon"},
]

load_book_list_file.load_book_list(book_list)
load_book_list_file.load_book_list_borrowed(book_list_borrowed)


def update_book():
    # Select

    found_search_result = False

    search_term = input("Enter name to update: ")
    for index, book in enumerate(book_list):
        if search_term.lower() in book["name"].lower():
            found_search_result = True
            print(f"{index+1}. {book['name']} - {book['phone']}")

    if not found_search_result:
        print("No item found")
        return

    selected_index = int(input("Enter a book to update: "))

    new_name = input("Enter new name: ")
    new_phone = input("Enter new phone number: ")
    new_email = input("Enter new email: ")

    book_list[selected_index - 1].update(
        {"name": new_name, "phone": new_phone, "email": new_email}
    )

    print("book successfully updated!")


print(
    messages_file.hello_message, messages_file.welcome_message, messages_file.book_art
)


# Infinite Menu
while True:
    print(messages_file.menu_text)
    choice = input(">> Enter your choice: ")
    # print("\n")

    if choice == "1":
        view_book_list_file.view_book_list(book_list)
    elif choice == "2":
        view_borrowed_books_file.view_borrowed_book_list(book_list_borrowed)
    elif choice == "3":
        search_books_title_isbn_file.search_books_title_isbn(book_list)
    elif choice == "4":
        search_books_author_file.search_books_author(book_list)
    elif choice == "5":
        book_list = add_book_file.add_book(book_list)
    elif choice == "6":
        book_list = remove_book_file.remove_book(book_list)
    elif choice == "7":
        pass
        # book_list, book_list_borrowed = lend_book_file.lend_book(book_list, book_list_borrowed)
    elif choice == "8":
        pass
        # book_list, book_list_borrowed = return_book_file.return_book(book_list, book_list_borrowed)
    elif choice == "9":
        save_book_file.save_books(book_list)
        save_book_file.save_books_borrowed(book_list_borrowed)
        print("\n Books saved successfully!")
    elif choice == "10":
        pass
        book_list = reset_system_file.reset_book_list(book_list)
        book_list_borrowed = reset_system_file.reset_book_list_borrowed(
            book_list_borrowed
        )
        print(messages_file.reset_message)
    elif choice == "0":
        print(
            "\n Exiting...\n\n Thank you for using our service!",
            "\n",
            messages_file.bye_message,
        )
        break
    else:
        print(messages_file.invalid_choice_message)
