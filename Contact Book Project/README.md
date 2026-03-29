# 📞 Contact Book in Python

A simple **Command-Line Contact Book Application** built using Python.  
This project demonstrates the use of **List, Dictionary, Tuple, and Set** data structures along with functions, loops, and conditional statements.

---

## 📌 Features

- ➕ Add new contacts
- 📋 View all contacts
- 🔍 Search contact by name
- 🗑️ Delete contact using **name and phone number**
- 🏷️ Add tags to categorize contacts (friend, office, family, etc.)
- ♻️ Prevent duplicate tags using Set

---

## 🧠 Concepts Used

| Concept | Usage |
|--------|------|
| List | Store multiple contacts |
| Dictionary | Store contact details |
| Tuple | Store fixed phone structure (country code + number) |
| Set | Store unique tags |
| Functions | Organize code into reusable blocks |
| Loop | Continuous menu system |
| Conditional statements | Decision making |
| String methods | Case-insensitive search |

---

## 📂 Data Structures Used

### List
Stores all contacts:

```python
contacts = []
```

---

### Dictionary
Stores each contact's details:

```python
contact = {
    "name": "Siva",
    "email": "siva@gmail.com"
}
```

---

### Tuple
Stores phone number in fixed structure:

```python
("+91", "9876543210")
```

---

### Set
Stores unique tags:

```python
{"friend", "office"}
```

---

## 💻 Example Contact

```python
{
    "name": "Siva",
    "phone": ("+91", "9876543210"),
    "email": "siva@gmail.com",
    "tags": {"friend", "college"}
}
```

---

## 💻 Project Code

```python
contacts = []

def add_contact():
    name = input("Enter name: ")
    
    phone = input("Enter phone number: ")
    country_code = "+91"
    
    email = input("Enter email: ")
    tags = set(input("Enter tags (comma separated): ").split(","))
    
    contact = {
        "name": name,
        "phone": (country_code, phone),
        "email": email,
        "tags": tags
    }
    
    contacts.append(contact)
    print("Contact added successfully\n")


def view_contacts():
    if not contacts:
        print("No contacts available\n")
        return
    
    for index, c in enumerate(contacts):
        print(f"""
Contact {index+1}
Name: {c['name']}
Phone: {c['phone'][0]} {c['phone'][1]}
Email: {c['email']}
Tags: {c['tags']}
""")


def search_contact():
    search_name = input("Enter name to search: ")
    
    for c in contacts:
        if c["name"].lower() == search_name.lower():
            print("Contact Found:")
            print(c)
            return
    
    print("Contact not found\n")


def delete_contact():
    name = input("Enter name to delete: ").lower()
    phone = input("Enter phone number to delete: ")
    
    for c in contacts:
        if c["name"].lower() == name and c["phone"][1] == phone:
            contacts.remove(c)
            print("Contact deleted successfully\n")
            return
    
    print("No matching contact found\n")


while True:
    print("==== CONTACT BOOK ====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_contact()
        
    elif choice == "2":
        view_contacts()
        
    elif choice == "3":
        search_contact()
        
    elif choice == "4":
        delete_contact()
        
    elif choice == "5":
        break
        
    else:
        print("Invalid choice\n")
```

---

## ▶️ How to Run the Program

1. Install Python
2. Save file as:

```
contact_book.py
```

3. Run the program:

```
python contact_book.py
```

---

## 📷 Sample Menu

```
==== CONTACT BOOK ====
1. Add Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Exit
```

---

## 🎯 Learning Outcome

Through this project, I learned:

- How to use Python data structures in real applications
- How to organize programs using functions
- How to take user input and process data
- How to apply logic for search and delete operations
- Practical use of List, Dictionary, Tuple, and Set

---

## 🚀 Future Improvements

- Edit contact feature
- Save contacts to file (JSON)
- GUI version using Tkinter
- Import/export contacts
- Search by tags

---

## 🧑‍💻 Author

[**Sivakumar**](https://github.com/sandhipeta/python_projects/blob/main/Contact%20Book%20Project/contact_book.py)

Learning Python step by step by building practical projects.
