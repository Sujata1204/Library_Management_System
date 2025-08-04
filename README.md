# 📚 Library Management System – Console-Based Application 🏛️

Hello! I'm **Sujata 👩‍💻**, and this project is a **Python + MySQL-based Library Management System**, designed to simplify the operations of a library — including managing members, issuing and returning books, handling feedback, and tracking book status.

---

## 🎓 Learning Outcome

To build a **smart, terminal-based library system** that efficiently handles the following:

- ✅ Book cataloging and availability tracking
- ✅ Member registration and membership renewal
- ✅ Book issuing and return handling
- ✅ Review system for book feedback
- ✅ Dashboard-style summary for key metrics

---

## 🏗️ Project Foundation

| Layer        | Technology                |
|--------------|----------------------------|
| 👩‍💻 Programming | Python (Console UI)        |
| 🗄️ Database     | MySQL                      |
| 🔗 Connector   | mysql-connector-python     |
| 🧰 IDE         | Visual Studio Code (VS Code) |

--- 
---

## 📋 Main Modules

| 🔧 Feature                | 📋 Description                                                                 |
|--------------------------|---------------------------------------------------------------------------------|
| 📚 **Add New Books**        | Add books with title, author, and default availability                        |
| 🧑‍💼 **Register Members**    | Add members with automatic membership and expiry tracking                     |
| 🔁 **Issue/Return Books**   | Handles issuing books (if available) and returning books                      |
| 🧾 **Feedback System**      | Users can rate books and provide feedback                                     |
| 🛑 **Update Book Status**   | Mark books as *Lost*, *Stolen*, or *Weeded-Out* with availability control     |
| ♻️ **Renew Memberships**    | Extend expiry date for registered members                                     |

---

## 📽️ System in Motion

Take a quick tour of how the system works — from issuing books to managing members!

👉 [**Python + MySQL Library App – Step-by-Step vedio guide**](https://drive.google.com/file/d/1kINlgAZCys66Cv7cbUBi4Jv85A5iYADv/view?usp=drive_link)

---

## 🔄 System Workflow

1. 🏁 **📄 View main.py Script**

   **[https://drive.google.com/file/d/1SkRe65N0Z1kzjRI_eILDWNH7MkzKfRX9/view?usp=drive_link]**

2. 🧭 **Main Menu Appears**
   - Choose from:
     - Library Menu (view available books, stats)
     - Member Records (view or add members)
     - Manage Records (add books/members)
     - Issue or Return Section
     - Membership Management
     - Book Rating and Feedback
     - Update Book Status

3. 📚 **Add or View Books**
   - Add new book entries with title and author.
   - Books are stored in the MySQL `books` table.

4. 🧑‍💼 **Register New Members**
   - Collect name, DOB, and address.
   - Automatically assign membership and expiry dates.

5. 🔁 **Issue or Return Books**
   - Issue books only if `status = Available`
   - Automatically records issue date and due date.
   - On return, the status is reset to `Available`.

6. 📝 **Submit Book Feedback**
   - Users can submit a rating (1–5) and optional comments.

7. 🛠️ **Update Book Status**
   - Mark books as **Lost**, **Stolen**, or **Weeded-Out**
   - Automatically sets availability to "No" 

8. 📅 **Renew Memberships**
   - Select a member to extend their membership for another year.

9. 🚪 **Exit Program**
    - All connections to the MySQL database are properly closed.


---

---

## 📂 Project Structure
📁 Library_Management_System/
├── 📄 library_management.py   # Main program file
├── 📄 README.md               # Documentation
└── 🗃️ MySQL Tables             # Created from within the code (auto-setup)

--- 
## 🧠 Key Concepts Learned

🔗 Database Integration with MySQL and Python

🔄 Real-world CRUD operations (Create, Read, Update, Delete)

📅 Date handling using Python datetime and timedelta

🔎 Dynamic search and filtering using SQL queries

🎯 Console UI design using menus and conditional logic

----

## 🙏 Acknowledgment
Special thanks to **SkillCircle** Institute and my mentor **Miss Sheetal Gupta** for their constant support and guidance.

## 🤝 Connect with Me

I'm open to collaborations, internships, and data-driven opportunities. Let's connect!

📧 **Email** : [sujataattri5@gmail.com]

💼 **LinkedIn** : [www.linkedin.com/in/sujata-ab727236a]

🐙 **GitHub** : [https://github.com/Sujata1204]

## ⭐️ Show Some Love
If you found this helpful, please ⭐ the repo and share your feedback!

**💬 Share suggestions or improvements**

## “A library is not a luxury but one of the necessities of life.” – Henry Ward Beecher
