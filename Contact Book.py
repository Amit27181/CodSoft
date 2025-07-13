import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []

def refresh_listbox():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

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

def view_contact(event):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        messagebox.showinfo("📇 Contact Details",
            f"👤 Name: {contact['name']}\n"
            f"📞 Phone: {contact['phone']}\n"
            f"📧 Email: {contact['email']}\n"
            f"🏠 Address: {contact['address']}"
        )

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

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Window setup
root = tk.Tk()
root.title("📘 Contact Book")
root.geometry("600x400")
root.config(bg="#e6f2ff")

# Labels and entry fields
label_font = ("Arial", 10, "bold")
entry_bg = "#ffffff"

tk.Label(root, text="Name", font=label_font, bg="#e6f2ff").grid(row=0, column=0, sticky="w", padx=10)
name_entry = tk.Entry(root, bg=entry_bg)
name_entry.grid(row=0, column=1, pady=5, padx=5)

tk.Label(root, text="Phone", font=label_font, bg="#e6f2ff").grid(row=1, column=0, sticky="w", padx=10)
phone_entry = tk.Entry(root, bg=entry_bg)
phone_entry.grid(row=1, column=1, pady=5, padx=5)

tk.Label(root, text="Email", font=label_font, bg="#e6f2ff").grid(row=2, column=0, sticky="w", padx=10)
email_entry = tk.Entry(root, bg=entry_bg)
email_entry.grid(row=2, column=1, pady=5, padx=5)

tk.Label(root, text="Address", font=label_font, bg="#e6f2ff").grid(row=3, column=0, sticky="w", padx=10)
address_entry = tk.Entry(root, bg=entry_bg)
address_entry.grid(row=3, column=1, pady=5, padx=5)

# Buttons
button_font = ("Arial", 10, "bold")
tk.Button(root, text="➕ Add Contact", command=add_contact, bg="#4CAF50", fg="white", font=button_font).grid(row=4, column=0, columnspan=2, pady=10)

# Contact list
listbox = tk.Listbox(root, width=40, height=15, bg="#f9f9f9", font=("Arial", 10))
listbox.grid(row=0, column=2, rowspan=8, padx=15, pady=5)
listbox.bind("<Double-1>", view_contact)

# Search section
search_entry = tk.Entry(root, width=20, bg="#fffacd")
search_entry.grid(row=5, column=0, columnspan=2, padx=5)
tk.Button(root, text="🔍 Search", command=search_contact, bg="#2196F3", fg="white", font=button_font).grid(row=5, column=2, sticky="w")

# Update and Delete buttons
tk.Button(root, text="✏️ Update", command=update_contact, bg="#ff9800", fg="white", font=button_font).grid(row=6, column=0, pady=5)
tk.Button(root, text="🗑️ Delete", command=delete_contact, bg="#f44336", fg="white", font=button_font).grid(row=6, column=1, pady=5)

root.mainloop()

