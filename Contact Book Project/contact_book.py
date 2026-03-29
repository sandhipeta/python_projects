contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    country_code = "+91"
    emali = input("Enter email: ")
    tags = set(input("Enter tags (Comma separated): ").split(","))
    
    contact = {
        "name": name,
        "phone": (country_code, phone),
        "email": emali,
        "tags": tags
    }
    
    contacts.append(contact)
    
    print("Contact added successfully\n")

def view_contacts():
    if not contacts:
        print("No contacts available\n")
        return
    
    for index, contact in enumerate(contacts):
        print(f"Contact {index+1} Name: {contact['name']} Phone: {contact['phone'][0]} {contact['phone'][1]} Email: {contact['email']} Tags: {contact['tags']}")

def search_contact():
    search_name = input("Enter name to search: ")
    
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            print("Contact found: ")
            print(contact)
            return
        print("Contact not found\n")

def delete_contact():
    view_contacts()
    
    name = input("Enter name to delete: ").lower()
    phone = input("Enter phone number to delete: ")
    
    for c in contacts:
        
        if c['name'].lower() == name and c['phone'][1] == phone:
            contacts.remove(c)
            print("Contact deleted sucessfully\n")
            return
        print("No matching found\n")
        
    

while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
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
        pass
    elif choice == "5":
        break
    else:
        print("Invalid Choice\n")