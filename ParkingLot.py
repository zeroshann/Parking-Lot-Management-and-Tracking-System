'''Parking Lot Monitoring and Tracking System

    This application is a GUI-based Parking Lot Monitoring and Tracking System developed using python and Tkinter.
It allows user to manage parking space efficiently by tracking vehicle entries and exits in parking lot.

Author:
Kristian Shine Carro
'''

import tkinter as tk
from tkinter import ttk, messagebox

capacity = 0
vehicles = []

def save_file():
    with open("Parking.txt", "w") as file:
        for v in vehicles:
            file.write(v + "\n" )
            
def load_file():
    try:
        with open("Parking.txt", "r") as file:
            for line in file:
                plate = line.strip()
                if plate and plate not in vehicles:
                    vehicles.append(plate)
                    tree.insert("", "end", values=(plate,))                 
    except:
        pass

def log_history(action, plate): 
    with open("log.txt", "a") as file:
        file.write(f"{action}: {plate}\n")
        
#======Function======
def set_capacity():
    global capacity
    try:
        capacity = int(cap_entry.get())
        cap_label.config(text=f"Capacity: {capacity}")
        update_status()
    except:
        messagebox.showerror("Error!", "Set a valid number.")
        
def vehicle_entry():
    global vehicles
    plate = plate_entry.get()
    
    if capacity == 0:
        messagebox.showwarning("Warning", "Set capacity first!")
    elif len(vehicles) >= capacity:
        messagebox.showwarning("Full", "Parking lot is currently full!")
    elif plate in vehicles:
        messagebox.showwarning("Duplicate", "Vehicle is already inside.")
    elif plate == "":
        messagebox.showwarning("Input Error", "Enter plate number.")
    else:
        vehicles.append(plate) #add vehicle to list
        tree.insert("", "end", values=(plate,))
        plate_entry.delete(0, tk.END)
        
        save_file()
        log_history("ENTRY", plate)
        
        update_status()
        
def vehicle_exit():
    global vehicles
    plate = plate_entry.get()
    
    if plate in vehicles:
        vehicles.remove(plate) #remove from list
        
        for item in tree.get_children():
            if tree.item(item)["values"][0] == plate:
                tree.delete(item)
                break
            
        save_file()
        log_history("EXIT", plate)
        
        update_status()
    else:
        messagebox.showerror("Error", "Vehicle was not found")    
        
def update_status():
    occupied = len(vehicles)
    available = capacity - occupied 
    
    status_label.config(
        text=f"Occupied: {occupied} | Available: {available}"
    )       
    
    #update progress bar
    if capacity > 0:
        percentage = (occupied / capacity) * 100
        progress['value'] = percentage
    else:
        progress['value'] = 0
        
# Main Window
root = tk.Tk()
root.title("Parking Lot System")
root.geometry("500x400")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text="Parking")
notebook.add(frame2, text="Status")

#tab 1
ttk.Label(frame1, text="Set capacity").pack(pady=5)

cap_entry = ttk.Entry(frame1)
cap_entry.pack()

ttk.Button(frame1, text="Set", command=set_capacity).pack(pady=5)

cap_label = ttk.Label(frame1, text="Capacity: 0")
cap_label.pack()

ttk.Label(frame1, text="Plate Number").pack(pady=5)

plate_entry = ttk.Entry(frame1)
plate_entry.pack()

ttk.Button(frame1, text="Vehicle Entry", command=vehicle_entry).pack(pady=5)
ttk.Button(frame1, text="Vehicle Exit", command=vehicle_exit).pack(pady=5)

tree = ttk.Treeview(frame1, columns=("plate",), show="headings")
tree.heading("plate", text="Plate Number")
tree.pack(pady=10)

#tab2 
status_label = ttk.Label(frame2, text="Occupied: 0 | Available: 0")
status_label.pack(pady=10)

progress = ttk.Progressbar(frame2, maximum=100)
progress.pack(pady=20)

load_file()
update_status()

root.mainloop()