#Definning list
books = ["To Kill a Mockingbird", "1984", "The Great Gatsby", "Moby Dick", "Pride and Prejudice"]

def display_books():
    for book in books:
        print(book)

#Adding new element
def add_book():
    book_name = input("Enter the book name to add to the list: " )
    books.append(book_name)

#updating list
def update_book():
    current_title = input("Enter the current book name: " )
    new_title = input("Enter the new book name: " )
    found = False
    for index in range(len(books)):
        if books[index] == current_title:
            books[index] = new_title
            print(current_title +" changed to "+ new_title)
            found = True
            break
    if not found:
        print("Book name is incorrect or is not present in the list :(")

#deleting element
def delete_book():
    del_book_name = input("Enter the book name you want to delete: ")
    found = False
    for index in range(len(books)):
        if books[index] == del_book_name:
            books.pop(index)
            print(del_book_name +" deleted from the list")
            found = True
            break
    if not found:
        print("Book name is incorrect or is not present in the list :(")

#Main function
def main():
    while True:
        print("\nMenu:")
        print("1. Display all books")
        print("2. Add a new book")
        print("3. Update a book")
        print("4. Delete a book")
        print("5. Exit")
        
        choice = input("Please enter your choice (1-5): ")
        
        if choice == "1":
            display_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
