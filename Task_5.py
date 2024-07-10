#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

def create_db():
    conn = sqlite3.connect('billing.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            total_price REAL,
            FOREIGN KEY(customer_id) REFERENCES customers(id),
            FOREIGN KEY(product_id) REFERENCES products(id)
        )
    ''')
    
    conn.commit()
    conn.close()

# Run the function to create the database
create_db()
print("Database created and tables are set up.")


# In[ ]:


import tkinter as tk
from tkinter import messagebox
import sqlite3

def add_customer():
    name = entry_name.get()
    contact = entry_contact.get()
    if name and contact:
        conn = sqlite3.connect('billing.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO customers (name, contact) VALUES (?, ?)', (name, contact))
        conn.commit()
        conn.close()
        entry_name.delete(0, tk.END)
        entry_contact.delete(0, tk.END)
        messagebox.showinfo("Success", "Customer added successfully!")
    else:
        messagebox.showerror("Error", "Please fill in all fields")

def add_product():
    name = entry_product_name.get()
    price = entry_price.get()
    if name and price:
        conn = sqlite3.connect('billing.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, float(price)))
        conn.commit()
        conn.close()
        entry_product_name.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        messagebox.showinfo("Success", "Product added successfully!")
    else:
        messagebox.showerror("Error", "Please fill in all fields")
        
def generate_invoice():
    customer_id = entry_customer_id.get()
    product_id = entry_product_id.get()
    quantity = entry_quantity.get()
    if customer_id and product_id and quantity:
        conn = sqlite3.connect('billing.db')
        cursor = conn.cursor()
        cursor.execute('SELECT price FROM products WHERE id=?', (product_id,))
        product = cursor.fetchone()
        if product:
            total_price = float(product[0]) * int(quantity)
            cursor.execute('INSERT INTO transactions (customer_id, product_id, quantity, total_price) VALUES (?, ?, ?, ?)', 
                           (customer_id, product_id, quantity, total_price))
            conn.commit()
            conn.close()
            entry_customer_id.delete(0, tk.END)
            entry_product_id.delete(0, tk.END)
            entry_quantity.delete(0, tk.END)
            messagebox.showinfo("Success", "Invoice generated successfully!")
        else:
            messagebox.showerror("Error", "Product not found")
    else:
        messagebox.showerror("Error", "Please fill in all fields")

app = tk.Tk()
app.title("Billing Software")

# Customer Details
frame_customer = tk.Frame(app)
frame_customer.pack(pady=10)

tk.Label(frame_customer, text="Customer Name").grid(row=0, column=0)
entry_name = tk.Entry(frame_customer)
entry_name.grid(row=0, column=1)

tk.Label(frame_customer, text="Contact").grid(row=1, column=0)
entry_contact = tk.Entry(frame_customer)
entry_contact.grid(row=1, column=1)

btn_add_customer = tk.Button(frame_customer, text="Add Customer", command=add_customer)
btn_add_customer.grid(row=2, columnspan=2, pady=10)

# Product Details
frame_product = tk.Frame(app)
frame_product.pack(pady=10)

tk.Label(frame_product, text="Product Name").grid(row=0, column=0)
entry_product_name = tk.Entry(frame_product)
entry_product_name.grid(row=0, column=1)

tk.Label(frame_product, text="Price").grid(row=1, column=0)
entry_price = tk.Entry(frame_product)
entry_price.grid(row=1, column=1)

btn_add_product = tk.Button(frame_product, text="Add Product", command=add_product)
btn_add_product.grid(row=2, columnspan=2, pady=10)

# Invoice Generation
frame_invoice = tk.Frame(app)
frame_invoice.pack(pady=10)

tk.Label(frame_invoice, text="Customer ID").grid(row=0, column=0)
entry_customer_id = tk.Entry(frame_invoice)
entry_customer_id.grid(row=0, column=1)

tk.Label(frame_invoice, text="Product ID").grid(row=1, column=0)
entry_product_id = tk.Entry(frame_invoice)
entry_product_id.grid(row=1, column=1)

tk.Label(frame_invoice, text="Quantity").grid(row=2, column=0)
entry_quantity = tk.Entry(frame_invoice)
entry_quantity.grid(row=2, column=1)

btn_generate_invoice = tk.Button(frame_invoice, text="Generate Invoice", command=generate_invoice)
btn_generate_invoice.grid(row=3, columnspan=2, pady=10)

# Run the application
app.mainloop()


# In[ ]:


# Save the GUI code to a file
gui_code = """
import tkinter as tk
from tkinter import messagebox
import sqlite3

def add_customer():
    name = entry_name.get()
    contact = entry_contact.get()
    if name and contact:
        conn = sqlite3.connect('billing.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO customers (name, contact) VALUES (?, ?)', (name, contact))
        conn.commit()
        conn.close()
        entry_name.delete(0, tk.END)
        entry_contact.delete(0, tk.END)
        messagebox.showinfo("Success", "Customer added successfully!")
    else:
        messagebox.showerror("Error", "Please fill in all fields")

def add_product():
    name = entry_product_name.get()
    price = entry_price.get()
    if name and price:
        conn = sqlite3.connect('billing.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, float(price)))
        conn.commit()
        conn.close()
        entry_product_name.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        messagebox.showinfo("Success", "Product added successfully!")
    else:
        messagebox.showerror("Error", "Please fill in all fields")

def generate_invoice():
    customer_id = entry_customer_id.get()
    product_id = entry_product_id.get()
    quantity = entry_quantity.get()
    if customer_id and product_id and quantity:
        conn = sqlite3.connect('billing.db')
        cursor = conn.cursor()
        cursor.execute('SELECT price FROM products WHERE id=?', (product_id,))
        product = cursor.fetchone()
        if product:
            total_price = float(product[0]) * int(quantity)
            cursor.execute('INSERT INTO transactions (customer_id, product_id, quantity, total_price) VALUES (?, ?, ?, ?)', 
                           (customer_id, product_id, quantity, total_price))
            conn.commit()
            conn.close()
            entry_customer_id.delete(0, tk.END)
            entry_product_id.delete(0, tk.END)
            entry_quantity.delete(0, tk.END)
            messagebox.showinfo("Success", "Invoice generated successfully!")
        else:
            messagebox.showerror("Error", "Product not found")
    else:
        messagebox.showerror("Error", "Please fill in all fields")

app = tk.Tk()
app.title("Billing Software")

# Customer Details
frame_customer = tk.Frame(app)
frame_customer.pack(pady=10)

tk.Label(frame_customer, text="Customer Name").grid(row=0, column=0)
entry_name = tk.Entry(frame_customer)
entry_name.grid(row=0, column=1)

tk.Label(frame_customer, text="Contact").grid(row=1, column=0)
entry_contact = tk.Entry(frame_customer)
entry_contact.grid(row=1, column=1)

btn_add_customer = tk.Button(frame_customer, text="Add Customer", command=add_customer)
btn_add_customer.grid(row=2, columnspan=2, pady=10)

# Product Details
frame_product = tk.Frame(app)
frame_product.pack(pady=10)

tk.Label(frame_product, text="Product Name").grid(row=0, column=0)
entry_product_name = tk.Entry(frame_product)
entry_product_name.grid(row=0, column=1)

tk.Label(frame_product, text="Price").grid(row=1, column=0)
entry_price = tk.Entry(frame_product)
entry_price.grid(row=1, column=1)

btn_add_product = tk.Button(frame_product, text="Add Product", command=add_product)
btn_add_product.grid(row=2, columnspan=2, pady=10)

# Invoice Generation
frame_invoice = tk.Frame(app)
frame_invoice.pack(pady=10)

tk.Label(frame_invoice, text="Customer ID").grid(row=0, column=0)
entry_customer_id = tk.Entry(frame_invoice)
entry_customer_id.grid(row=0, column=1)

tk.Label(frame_invoice, text="Product ID").grid(row=1, column=0)
entry_product_id = tk.Entry(frame_invoice)
entry_product_id.grid(row=1, column=1)

tk.Label(frame_invoice, text="Quantity").grid(row=2, column=0)
entry_quantity = tk.Entry(frame_invoice)
entry_quantity.grid(row=2, column=1)

btn_generate_invoice = tk.Button(frame_invoice, text="Generate Invoice", command=generate_invoice)
btn_generate_invoice.grid(row=3, columnspan=2, pady=10)

app.mainloop()
"""

with open("billing_app.py", "w") as file:
    file.write(gui_code)

print("GUI application code saved to billing_app.py")


# In[ ]:


python billing_app.py


# In[ ]:




