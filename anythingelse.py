# %%
import tkinter as tk
import pickle
import pandas as pd
users = {"Prateek": [11814621, 0], "Neev": [11814121, 2], "Sai": [11804123, 4]}


# %%
db = open("users.pickle", "wb")
pickle.dump(users, db)
db.close()

# %%
db_open = open("users.pickle", "rb")
check = pickle.load(db_open)
db_open.close()


# %%
users = {"Prateek": [11814621, 22], "Neev": 11814121, "Sai": 11804123}

# %%
categories = {"count": 3, "names": [
    "Variable Names", "Core Data Types", "Advanced Formatting"]}

db_open = open("categories.pickle", "wb")
pickle.dump(categories, db_open)
db_open.close()
# %%
variable_names = [{"question": "Is Python case sensitive when dealing with identifiers?", "options": ("yes", "no", "machine dependent", "none of the mentioned"), "answer": 0}, {
    "question": "What is the maximum possible length of an identifier?", "options": ("31 characters", "63 characters", "79 characters", "none of the mentioned"), "answer": 3}]

# %%

# %%


def tell(e):
    p = listbox.curselection()
    label.config(text="You have selected " + str(p[0]))


root = tk.Tk()
label = tk.Label(root, text="Test")
listbox = tk.Listbox(root)
listbox.insert(0, "First")
listbox.insert(1, "Second")
listbox.insert(2, "Third")
listbox.bind("<ButtonRelease-1>", tell)
label.pack()
listbox.pack()

root.mainloop()

# %%
variable_names = [{"question": "Is Python case sensitive when dealing with identifiers?", "options": ("yes", "no", "machine dependent", "none of the mentioned"), "answer": 0}, {
    "question": "What is the maximum possible length of an identifier?", "options": ("31 characters", "63 characters", "79 characters", "none of the mentioned"), "answer": 3}]

db_open = open("Variable Names.pickle", "wb")
pickle.dump(variable_names, db_open)
db_open.close()

# %%
len(variable_names)

# %%
type(variable_names[0]["options"][0])

# %%