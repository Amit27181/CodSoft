# # Contact Book Program

# contacts = []

# # Add a new contact
# def add_contact():
#     name = input("Enter name: ")
#     phone = input("Enter phone number: ")
#     email = input("Enter email: ")
#     address = input("Enter address: ")
#     contacts.append({
#         "name": name,
#         "phone": phone,
#         "email": email,
#         "address": address
#     })
#     print("Contact added successfully.\n")

# # View all contacts
# def view_contacts():
#     if not contacts:
#         print("No contacts found.\n")
#         return
#     print("\n--- Contact List ---")
#     for i, contact in enumerate(contacts, start=1):
#         print(f"{i}. {contact['name']} - {contact['phone']}")
#     print()

# # Search contact by name or phone number
# def search_contact():
#     query = input("Enter name or phone number to search: ")
#     found = False
#     for contact in contacts:
#         if contact["name"] == query or contact["phone"] == query:
#             print("\n--- Contact Found ---")
#             print(f"Name: {contact['name']}")
#             print(f"Phone: {contact['phone']}")
#             print(f"Email: {contact['email']}")
#             print(f"Address: {contact['address']}\n")
#             found = True
#             break
#     if not found:
#         print("Contact not found.\n")

# # Update contact
# def update_contact():
#     name = input("Enter the name of the contact to update: ")
#     for contact in contacts:
#         if contact["name"] == name:
#             print("Leave blank to keep existing value.")
#             contact["phone"] = input(f"New phone [{contact['phone']}]: ") or contact["phone"]
#             contact["email"] = input(f"New email [{contact['email']}]: ") or contact["email"]
#             contact["address"] = input(f"New address [{contact['address']}]: ") or contact["address"]
#             print("Contact updated successfully.\n")
#             return
#     print("Contact not found.\n")

# # Delete contact
# def delete_contact():
#     name = input("Enter the name of the contact to delete: ")
#     for contact in contacts:
#         if contact["name"] == name:
#             contacts.remove(contact)
#             print("Contact deleted successfully.\n")
#             return
#     print("Contact not found.\n")

# # Main menu
# def main():
#     while True:
#         print("------ Contact Book ------")
#         print("1. Add Contact")
#         print("2. View Contacts")
#         print("3. Search Contact")
#         print("4. Update Contact")
#         print("5. Delete Contact")
#         print("6. Exit")
#         choice = input("Enter your choice (1-6): ")

#         if choice == "1":
#             add_contact()
#         elif choice == "2":
#             view_contacts()
#         elif choice == "3":
#             search_contact()
#         elif choice == "4":
#             update_contact()
#         elif choice == "5":
#             delete_contact()
#         elif choice == "6":
#             print("Exiting Contact Book. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Try again.\n")

# # Run the program
# main()
import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []

# Function to refresh the listbox
def refresh_listbox():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Add contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showerror("Error", "Name and phone are required!")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    refresh_listbox()
    clear_entries()
    messagebox.showinfo("Success", "Contact added!")

# View selected contact
def view_contact(event):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        messagebox.showinfo("Contact Details",
            f"Name: {contact['name']}\n"
            f"Phone: {contact['phone']}\n"
            f"Email: {contact['email']}\n"
            f"Address: {contact['address']}"
        )

# Search contact
def search_contact():
    query = search_entry.get()
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == query.lower() or contact['phone'] == query:
            listbox.selection_clear(0, tk.END)
            listbox.selection_set(i)
            listbox.activate(i)
            listbox.see(i)
            view_contact(None)
            return
    messagebox.showinfo("Not Found", "Contact not found.")

# Update contact
def update_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        new_phone = simpledialog.askstring("Update Phone", "Enter new phone:", initialvalue=contact["phone"])
        new_email = simpledialog.askstring("Update Email", "Enter new email:", initialvalue=contact["email"])
        new_address = simpledialog.askstring("Update Address", "Enter new address:", initialvalue=contact["address"])

        if new_phone:
            contact["phone"] = new_phone
        if new_email:
            contact["email"] = new_email
        if new_address:
            contact["address"] = new_address

        refresh_listbox()
        messagebox.showinfo("Updated", "Contact updated.")
    else:
        messagebox.showerror("Error", "Select a contact to update.")

# Delete contact
def delete_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this contact?")
        if confirm:
            contacts.pop(index)
            refresh_listbox()
            messagebox.showinfo("Deleted", "Contact deleted.")
    else:
        messagebox.showerror("Error", "Select a contact to delete.")

# Clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("Contact Book")

# Entry fields
tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Phone").grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

tk.Label(root, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

tk.Label(root, text="Address").grid(row=3, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1)

tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, columnspan=2, pady=5)

# Contact listbox
listbox = tk.Listbox(root, width=40)
listbox.grid(row=0, column=2, rowspan=6, padx=10)
listbox.bind("<Double-1>", view_contact)

# Search bar
search_entry = tk.Entry(root)
search_entry.grid(row=6, column=0, columnspan=2)
tk.Button(root, text="Search", command=search_contact).grid(row=6, column=2)

# Buttons for update/delete
tk.Button(root, text="Update", command=update_contact).grid(row=7, column=0)
tk.Button(root, text="Delete", command=delete_contact).grid(row=7, column=1)

# Start GUI
root.mainloop()
