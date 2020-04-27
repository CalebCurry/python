def print_menu():
    print("""Choose a number: 
    1. Print all books
    2. Add a book
    3. Delete a book
    4. Update a book
    Q. QUIT""")

print("Hello, Welcome to your reading list.")
while(True):
    print_menu()
    response = int(input())
    if response == 1:
        print("Here are all of your books")
    elif response == 2:
        print("adding a book")
    elif response == 3:
        print("Deleting a book")
    elif response == 4:
        print("Updating a book")
    else:
        print("Good luck reading!")
        break


