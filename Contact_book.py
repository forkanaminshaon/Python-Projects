import csv
import os

CONTACTS_FILE = 'contacts.csv'

# Load contacts from file
def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    return contacts

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, mode='w', newline='') as file:
        fieldnames = ['Name', 'Phone', 'Email', 'Address']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

# Add a new contact
def add_contact(contacts):
    try:
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone Number: ").strip()
        if not phone.isdigit():
            raise ValueError("Phone number must be an integer.")
        email = input("Enter Email: ").strip()
        address = input("Enter Address: ").strip()

        for contact in contacts:
            if contact['Phone'] == phone:
                print("Error: Phone number already exists for another contact.")
                return

        contact = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
        contacts.append(contact)
        save_contacts(contacts)
        print("Contact added successfully!")
    except ValueError as ve:
        print("Error:", ve)

# View all contacts
def view_contacts(contacts):
    print("===== All Contacts =====")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. Name : {contact['Name']}")
        print(f"   Phone : {contact['Phone']}")
        print(f"   Email : {contact['Email']}")
        print(f"   Address: {contact['Address']}\n")
    print("========================")

# Search contact by any field
def search_contact(contacts):
    term = input("Enter search term (name/email/phone): ").strip().lower()
    found = False
    for contact in contacts:
        if (term in contact['Name'].lower() or
            term in contact['Email'].lower() or
            term in contact['Phone']):
            print("Search Result:")
            print(f"Name : {contact['Name']}")
            print(f"Phone : {contact['Phone']}")
            print(f"Email : {contact['Email']}")
            print(f"Address: {contact['Address']}\n")
            found = True
    if not found:
        print("No matching contact found.")

# Remove a contact by phone number
def remove_contact(contacts):
    phone = input("Enter the phone number of the contact to delete: ").strip()
    for contact in contacts:
        if contact['Phone'] == phone:
            confirm = input(f"Are you sure you want to delete contact number {phone}? (y/n): ").lower()
            if confirm == 'y':
                contacts.remove(contact)
                save_contacts(contacts)
                print("Contact deleted successfully!")
            return
    print("Contact not found.")

# Menu system
def menu():
    contacts = load_contacts()
    print("Welcome to the Contact Book CLI System!")
    print("Loading contacts from contacts.csv... Done!\n")

    while True:
        print("=========== MENU ===========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Exit")
        print("============================")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            remove_contact(contacts)
        elif choice == '5':
            print("Thank you for using the Contact Book CLI System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from the menu.")

if __name__ == '__main__':
    menu()
