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
            found = True
            break
    if not found:
        print("Book name is incorrect or is not present in the list :(")

