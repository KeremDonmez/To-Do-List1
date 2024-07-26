import tkinter as tk

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        feedback_label.config(text="Görev eklendi!", fg="green")
    else:
        feedback_label.config(text="Görev boş olamaz.", fg="red")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
        feedback_label.config(text="Görev silindi!", fg="green")
    except IndexError:
        feedback_label.config(text="Silmek için bir görev seçin.", fg="red")

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

feedback_label = tk.Label(root, text="", fg="red")
feedback_label.pack(pady=5)

root.mainloop()
