#
def add_student():
    print("You are on add student function")
    
def update_student():
    print("You are on update student function")
    
def delete_student():
    print("You are on delete student function")
    
def view_student():
    print("You are on view student function")
    
def take_student():
    print("You are on take student function")
    
def viewattendance_student():
    print("You are one view student function")
    
def menu():
    print("Enter 1 to add student")
    print("Enter 2 to update studend")
    print("Enter 3 to delete stuednt")
    print("Enter 4 to view student")
    print("Enter 5 to take attendance")
    print("Enter 6 to view attendance")
    print("Enter 7 to exist")

while True:
    menu()
    option = input("Enter menu no.")

    if option == "1":
        add_student()
    elif option == "2":
        update_student()
    elif option == "3":
        delete_student()
    elif option == "4":
        view_student()
    elif option == "5":
        take_student()
    elif option == "6":
        viewattendance_student()
    elif option == "7":
        print("Exit")
        break
    else:
        print("Invalid Option")
