import tkinter as tk
import csv
from tkinter import ttk
    
def search_database():
    roll_no = roll_no_entry.get()
    name = name_entry.get()
    branch = branch_entry.get()

    # Search in the CSV file
    with open('StudentData.csv', 'r') as file:
        csv_reader = csv.reader(file)
        found_results = []
        for row in csv_reader:
            if roll_no and roll_no in row[0]:
                found_results.append(row)
            elif name and name.upper() in row[1]:
                found_results.append(row)
            elif branch and branch.lower() in row[2].lower():
                found_results.append(row)

    # Find intersection of results
    filtered_results = []
    if found_results:
        filtered_results = found_results
        if name and branch and roll_no:
            filtered_results = [row for row in found_results if roll_no in row[0] and name.upper() in row[1] and branch.lower() in row[2].lower()]
        elif name and branch:
            filtered_results = [row for row in found_results if name.upper() in row[1] and branch.lower() in row[2].lower()]
        elif name and roll_no:
            filtered_results = [row for row in found_results if name.upper() in row[1] and roll_no in row[0]]
        elif branch and roll_no:
            filtered_results = [row for row in found_results if branch.lower() in row[2].lower() and roll_no in row[0]]

    
    # Display the results in the results_table
    clear_table()
    if filtered_results:
        for result in filtered_results:
            results_table.insert("", tk.END, values=result)
    else:
        results_table.insert("", tk.END, values=["No results found."])

def clear_table():
    results_table.delete(*results_table.get_children())

root = tk.Tk()
root.title("Student Database")
root.geometry("900x600")  # Set window size to 600x400 pixels

# Heading label
heading_label = tk.Label(root, text="Student Database", font=("Arial", 16, "bold"))
heading_label.pack(pady=10)

# Roll No input
roll_no_label = tk.Label(root, text="Roll No:")
roll_no_label.pack()
roll_no_entry = tk.Entry(root, width=40)
roll_no_entry.pack()

# Name input
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

# Branch input
branch_label = tk.Label(root, text="Branch:")
branch_label.pack()
branch_entry = tk.Entry(root, width=40)
branch_entry.pack()

# Search button
search_button = tk.Button(root, text="Search", command=search_database)
search_button.pack(pady=10)

# Results region (Table)
results_table = ttk.Treeview(root, columns=("Roll No", "Name", "Branch"), show="headings")
results_table.pack()

results_table.heading("Roll No", text="Roll No")
results_table.heading("Name", text="Name")
results_table.heading("Branch", text="Branch")

# Set column widths
results_table.column("Roll No", width=100)
results_table.column("Name", width=300)
results_table.column("Branch", width=400)

# Scrollbar for the results_table
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=results_table.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
results_table.configure(yscrollcommand=scrollbar.set)

# Footer
footer_label = tk.Label(root, text="@by AbhishekKumar", font=("Arial", 10))
footer_label.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
