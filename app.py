import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient
import csv

# MongoDB Connection
try:
    client = MongoClient("mongodb://hospital_system/")
    db = client["hospital_db"]
    collection = db["patients"]
except Exception as e:
    print(f"Connection Error: {e}")

# GUI Setup
root = tk.Tk()
root.title("Hospital Patient Management System")
root.geometry("1000x600")
root.configure(padx=20, pady=20)

# Variables
p_id = tk.StringVar()
p_name = tk.StringVar()
p_age = tk.StringVar()
p_gender = tk.StringVar()
p_blood = tk.StringVar()
p_doctor = tk.StringVar()
p_status = tk.StringVar()
search_var = tk.StringVar()

# Functions
def clear_fields():
    for var in [p_id, p_name, p_age, p_gender, p_blood, p_doctor, p_status]:
        var.set("")

def add_patient():
    if not p_id.get() or not p_name.get():
        messagebox.showerror("Error", "Patient ID and Name are required")
        return
    
    if collection.find_one({"p_id": p_id.get()}):
        messagebox.showerror("Error", "Patient ID already exists")
        return

    data = {
        "p_id": p_id.get(),
        "name": p_name.get(),
        "age": p_age.get(),
        "gender": p_gender.get(),
        "blood_group": p_blood.get(),
        "doctor": p_doctor.get(),
        "status": p_status.get()
    }
    collection.insert_one(data)
    view_patients()
    clear_fields()
    messagebox.showinfo("Success", "Patient Record Added")

def view_patients():
    for row in tree.get_children():
        tree.delete(row)
    for p in collection.find():
        tree.insert('', 'end', values=(p['p_id'], p['name'], p['age'], p['gender'], p['blood_group'], p['doctor'], p['status']))

def select_record(event):
    selected = tree.focus()
    if not selected: return
    values = tree.item(selected, 'values')
    vars_list = [p_id, p_name, p_age, p_gender, p_blood, p_doctor, p_status]
    for i in range(len(values)):
        vars_list[i].set(values[i])

def update_patient():
    collection.update_one(
        {"p_id": p_id.get()},
        {"$set": {
            "name": p_name.get(),
            "age": p_age.get(),
            "gender": p_gender.get(),
            "blood_group": p_blood.get(),
            "doctor": p_doctor.get(),
            "status": p_status.get()
        }}
    )
    view_patients()
    messagebox.showinfo("Updated", "Patient record updated successfully")

def delete_patient():
    if messagebox.askyesno("Confirm", "Are you sure you want to delete this record?"):
        collection.delete_one({"p_id": p_id.get()})
        view_patients()
        clear_fields()

def search_patient():
    for row in tree.get_children():
        tree.delete(row)
    query = {"name": {"$regex": search_var.get(), "$options": "i"}}
    for p in collection.find(query):
        tree.insert('', 'end', values=(p['p_id'], p['name'], p['age'], p['gender'], p['blood_group'], p['doctor'], p['status']))

# UI Layout (Input Form)
form_frame = tk.Frame(root)
form_frame.pack(side=tk.TOP, fill=tk.X)

labels = ["Patient ID", "Name", "Age", "Gender", "Blood Group", "Consulting Doctor", "Status"]
vars_list = [p_id, p_name, p_age, p_gender, p_blood, p_doctor, p_status]

for i, label in enumerate(labels):
    tk.Label(form_frame, text=label, font=('Arial', 10, 'bold')).grid(row=i//2, column=(i%2)*2, padx=10, pady=10, sticky="w")
    tk.Entry(form_frame, textvariable=vars_list[i], width=30).grid(row=i//2, column=(i%2)*2 + 1, padx=10, pady=10)

# Button Bar
btn_frame = tk.Frame(root)
btn_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

tk.Button(btn_frame, text="Add Patient", bg="green", fg="white", command=add_patient, width=15).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Update Record", bg="blue", fg="white", command=update_patient, width=15).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Delete Record", bg="red", fg="white", command=delete_patient, width=15).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Clear", command=clear_fields, width=10).pack(side=tk.LEFT, padx=5)

# Search Bar
search_frame = tk.Frame(root)
search_frame.pack(side=tk.TOP, fill=tk.X, pady=10)
tk.Label(search_frame, text="Search by Name:").pack(side=tk.LEFT, padx=5)
tk.Entry(search_frame, textvariable=search_var, width=30).pack(side=tk.LEFT, padx=5)
tk.Button(search_frame, text="Search", command=search_patient).pack(side=tk.LEFT, padx=5)

# Treeview (Table)
tree_frame = tk.Frame(root)
tree_frame.pack(fill=tk.BOTH, expand=True)

columns = ("ID", "Name", "Age", "Gender", "Blood", "Doctor", "Status")
tree = ttk.Treeview(tree_frame, columns=columns, show='headings')

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
tree.bind('<ButtonRelease-1>', select_record)

# Scrollbar
scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscrollcommand=scroll.set)

view_patients()
root.mainloop()
