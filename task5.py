import json

contacts = []

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts():
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts()
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ").lower()
    found_contacts = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    if not found_contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(found_contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def update_contact():
    search_term = input("Enter name or phone number of the contact to update: ").lower()
    found_contacts = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    
    if not found_contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(found_contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")
        
        choice = int(input("Enter the number of the contact to update: ")) - 1
        contact = found_contacts[choice]
        
        contact['name'] = input(f"Enter new name ({contact['name']}): ") or contact['name']
        contact['phone'] = input(f"Enter new phone number ({contact['phone']}): ") or contact['phone']
        contact['email'] = input(f"Enter new email ({contact['email']}): ") or contact['email']
        contact['address'] = input(f"Enter new address ({contact['address']}): ") or contact['address']
        
        save_contacts()
        print("Contact updated successfully!")

def delete_contact():
    search_term = input("Enter name or phone number of the contact to delete: ").lower()
    found_contacts = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    
    if not found_contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(found_contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")
        
        choice = int(input("Enter the number of the contact to delete: ")) - 1
        contact = found_contacts[choice]
        contacts.remove(contact)
        save_contacts()
        print("Contact deleted successfully!")

def main():
    global contacts
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
