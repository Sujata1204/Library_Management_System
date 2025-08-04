import mysql.connector
from datetime import datetime, timedelta

mycon=mysql.connector.connect(host="localhost",
                              user="root",
                              password="password",
                              database="library_management_system"
                              )
print(mycon)

mycursor=mycon.cursor()
# mycursor.execute("create database Library_Management_System")

# mycursor.execute('''CREATE TABLE IF NOT EXISTS books(
#                  Book_id INT PRIMARY KEY AUTO_INCREMENT,
#                  Book_Title VARCHAR(300),
#                  Author_Name Varchar(30),
#                  Book_Availability ENUM('yes','no') DEFAULT('yes'),
#                  status ENUM ("Available","Issued","Lost","Weeded_Out","Stolen") DEFAULT("Available"))''')


# mycursor.execute('''
#                  CREATE TABLE IF NOT EXISTS members(
#                     member_id INT PRIMARY KEY AUTO_INCREMENT,
#                     name VARCHAR(255),
#                     dob DATE,
#                     address VARCHAR (255),
#                     membership_date DATE,
#                     expiry_date DATE);
#                     ''')


# mycursor.execute('''CREATE TABLE IF NOT EXISTS issued_books (
#                     id INT PRIMARY KEY AUTO_INCREMENT,
#                     book_id INT,
#                     member_id INT,
#                     issue_date DATE,
#                     due_date DATE);
#                     ''')


# mycursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                      user_id INT PRIMARY KEY AUTO_INCREMENT,
#                      username VARCHAR(255),
#                      password VARCHAR(255),
#                      role ENUM('Admin', 'Librarian', 'Student'));
#                     ''')


# mycursor.execute('''CREATE TABLE IF NOT EXISTS book_reviews (
#                     review_id INT PRIMARY KEY AUTO_INCREMENT,
#                     book_id INT,
#                     rating INT CHECK(rating >= 1 AND rating <= 5),
#                     feedback TEXT);
#                     ''')

def view_all_registered_members():
    mycursor.execute("SELECT * FROM members")
    for row in mycursor.fetchall():
        print(row)


def add_new_member():
    name = input("Enter Member Name: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    address = input("Enter Address: ")
    membership_date = datetime.now().strftime('%Y-%m-%d')
    expiry_date = (datetime.now() + timedelta(days=365)).strftime('%Y-%m-%d')
    mycursor.execute("INSERT INTO members (name, dob, address, membership_date, expiry_date) VALUES (%s, %s, %s, %s, %s)",
                   (name, dob, address, membership_date, expiry_date))
    mycon.commit()
    print("New Member Added with Membership and Expiry Date.")


def add_new_book():
    Book_Title = input("Enter Book Title: ")
    Author_Name = input("Enter Author Name: ")
    mycursor.execute("INSERT INTO books (Book_Title, Author_Name, Book_Availability, status) VALUES (%s, %s, %s, %s)",
    (Book_Title, Author_Name, 'yes', 'Available'))
    mycon.commit()
    print("New Book Added Successfully.")


def renew_membership():
    member_id = input("Enter Member ID to renew: ")
    new_expiry_date = (datetime.now() + timedelta(days=365)).strftime('%Y-%m-%d')
    mycursor.execute("UPDATE members SET expiry_date = %s WHERE member_id = %s", (new_expiry_date, member_id))
    mycon.commit()
    print("Membership Renewed.")


def book_rating_feedback():
    book_id = input("Enter Book ID to rate: ")
    rating = int(input("Enter rating (1-5): "))
    feedback = input("Enter feedback: ")
    mycursor.execute("INSERT INTO book_reviews (book_id, rating, feedback) VALUES (%s, %s, %s)",
                   (book_id, rating, feedback))
    mycon.commit()
    print("Rating and Feedback Submitted.")


def top_rated_books():
    mycursor.execute("SELECT book_id, AVG(rating) as avg_rating FROM book_reviews GROUP BY book_id ORDER BY avg_rating DESC LIMIT 5")
    for row in mycursor.fetchall():
        print(f"Book ID: {row[0]}, Average Rating: {row[1]:.2f}")

def update_book_status():
    book_id = input("Enter Book ID to update status: ")
    print("Select New Status:")
    print("1. Lost")
    print("2. Stolen")
    print("3. Weeded-Out")
    choice = input("Enter choice (1-3): ")

    status_map = {'1': 'Lost', '2': 'Stolen', '3': 'Weeded-Out'}
    if choice in status_map:
        new_status = status_map[choice]
        mycursor.execute("UPDATE books SET status = %s, Book_Availability = 'No' WHERE Book_id = %s",
                         (new_status, book_id))
        mycon.commit()
        print(f"Book status updated to '{new_status}'.")
    else:
        print("Invalid choice.")


def record_menu():
    print("Available Books:")
    mycursor.execute("SELECT * FROM books WHERE  Book_Availability = 'Yes'")
    for row in mycursor.fetchall():
        print(row)
    print("Most Borrowed Books:")
    mycursor.execute("SELECT book_id, COUNT(*) as borrow_count FROM issued_books GROUP BY book_id ORDER BY borrow_count DESC LIMIT 5")
    for row in mycursor.fetchall():
        print(row)
    print("New Arrival Books:")
    mycursor.execute("SELECT * FROM books ORDER BY Book_id DESC LIMIT 5")
    for row in mycursor.fetchall():
        print(row)
    print("Top Rated Books:")
    top_rated_books()
    print("Lost Books Count:")
    mycursor.execute("SELECT COUNT(*) FROM books WHERE status = 'Lost'")
    print(mycursor.fetchone()[0])
    print("Stolen Books Count:")
    mycursor.execute("SELECT COUNT(*) FROM books WHERE status = 'Stolen'")
    print(mycursor.fetchone()[0])
    print("Weeded-Out Books Count:")
    mycursor.execute("SELECT COUNT(*) FROM books WHERE status = 'Weeded-Out'")
    print(mycursor.fetchone()[0])

def issue_book():
    book_id = input("Enter Book ID to issue: ")
    member_id = input("Enter Member ID: ")

    # Check book status before issuing
    mycursor.execute("SELECT status FROM books WHERE Book_id = %s", (book_id,))
    result = mycursor.fetchone()

    if result:
        status = result[0]
        if status == 'Available':
            issue_date = datetime.now().date()
            return_date = issue_date + timedelta(days=14)

            mycursor.execute("INSERT INTO issued_books (book_id, member_id, issue_date, return_date) VALUES (%s, %s, %s, %s)",
                             (book_id, member_id, issue_date, return_date))
            mycursor.execute("UPDATE books SET Book_Availability = 'No', status = 'Issued' WHERE Book_id = %s", (book_id,))
            mycon.commit()
            print("Book issued successfully.")
        else:
            print(f"Cannot issue book. Current status is '{status}'.")
    else:
        print("Book ID not found.")


def return_book():
    book_id = input("Enter Book ID to return: ")

    # Check current status
    mycursor.execute("SELECT status FROM books WHERE Book_id = %s", (book_id,))
    result = mycursor.fetchone()

    if result:
        current_status = result[0]
        if current_status == 'Issued':
            mycursor.execute("DELETE FROM issued_books WHERE book_id = %s", (book_id,))
            mycursor.execute("UPDATE books SET Book_Availability = 'Yes', status = 'Available' WHERE Book_id = %s", (book_id,))
            mycon.commit()
            print("Book returned successfully.")
        else:
            print(f"Cannot return the book. Current status is '{current_status}', not 'Issued'.")
    else:
        print("Book ID not found.")



def issue_or_return_menu():
    while True:
        print("\n--- Issue or Return Menu ---")
        print("1. Issue Book")
        print("2. Return Book")
        print("3. Back to Main Menu")
        ch = input("Enter your choice: ")
        if ch == '1':
            issue_book()
        elif ch == '2':
            return_book()
        elif ch == '3':
            break
        else:
            print("Invalid choice. Try again.")

# Main Menu Function

def main_menu():
    while True:
        print("\n=== Library Management System ===")  
        print("1. Library Menu")
        print("2. Member Record Menu")
        print("3. Manage Records")
        print("4. Issue or Return Section")
        print("5. Membership Management")
        print("6. Book Rating and Feedback")
        print("7. Update Book Status")
        print("8. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            record_menu()
        elif choice == '2':
            view_all_registered_members()
        elif choice == '3':
            print("\n--- Manage Records ---")
            print("1. Add New Member")
            print("2. Add New Book")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '1':
                add_new_member()
            elif sub_choice == '2':
                add_new_book()
            else:
                print("Invalid choice.")
        elif choice == '4':
             issue_or_return_menu()
        elif choice == '5':
            renew_membership()
        elif choice == '6':
            book_rating_feedback()
        elif choice == '7':
            update_book_status()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Try again.")

main_menu()

mycursor.close()
mycon.close()










































