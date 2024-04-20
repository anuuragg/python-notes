#Defining deictionary
library = {"Harper Lee" : {"To Kill a Mockingbird"}, "George Orwell" : {"1984"}, "F. Scott Fitzgerald" : {"The Great Gatsby"}, "Jane Austen" : {"Pride and Prejudice"}, "J.D. Salinger" : {"The Catcher in the Rye"}}

#Adding elements
def add_book(author, book):
    if author not in library:
        library[author] = set()
    library[author].add(book)
    
#Deleting elements
def delete_book(author, book):
    if author in library:
        if book in library[author]:
            library[author].remove(book)
        else:
            print(f"Book '{book}' not found for author '{author}'.")
    else:
        print(f"Author '{author}' not found in the library.")

#display function
def display_library():
    for author, books in library.items():
        print(f"Author: {author}")
        for book in books:
            print(f"  - {book}")

#Built-in functions
author_names = library.keys()
print("Authors in the library:", list(author_names))

book_sets = library.values()
print("Sets of books by authors:", list(book_sets))

author_book_pairs = library.items()
print("Authors and their books:", list(author_book_pairs))

books_by_author = library.get("Some Author", set())
print("Books by 'Some Author':", books_by_author)
