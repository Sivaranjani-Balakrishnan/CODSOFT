import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("600x600")
        self.root.configure(bg="#FFB6C1")

        # Page 1
        self.page_1 = tk.Frame(root, bg="#FFB6C1")

        self.label_welcome = tk.Label(self.page_1, text="Welcome to TO-DO List", font=("Helvetica", 20, "bold"), bg="#FFB6C1")
        self.label_welcome.pack(pady=20)

        self.label_quote = tk.Label(self.page_1, text="\"The best way to get something done is to begin\"", font=("Helvetica", 12), bg="#FFB6C1")
        self.label_quote.pack(pady=10)

        self.continue_button = tk.Button(self.page_1, text="Continue", command=self.show_page_2, bg="#FF69B4", fg="black")
        self.continue_button.pack(pady=20)

        # Page 2
        self.page_2 = tk.Frame(root, bg="#FFB6C1")

        self.label_add_task = tk.Label(self.page_2, text="Add Task", font=("Helvetica", 20, "bold"), bg="#FFB6C1")
        self.label_add_task.pack(pady=10)

        self.entry_task = tk.Entry(self.page_2, width=30, font=("Helvetica", 12))
        self.entry_task.pack(pady=10)
        self.entry_task.insert(0, "")

        self.add_task_button = tk.Button(self.page_2, text="Add Task", command=self.add_task, bg="#FF69B4", fg="black")
        self.add_task_button.pack(pady=10)

        self.task_display_frame = tk.Frame(self.page_2, bg="#FFB6C1")
        self.task_display_frame.pack(pady=10, anchor="w")

        self.task_count_label = tk.Label(self.page_2, text="You have 0 tasks to complete", font=("Helvetica", 12), bg="#FFB6C1")
        self.task_count_label.pack(pady=5)

        self.show_page_1()

        self.task_count = 0  

    def show_page_1(self):
        self.page_2.pack_forget()
        self.page_1.pack()

    def show_page_2(self):
        self.page_1.pack_forget()
        self.page_2.pack()

    def add_task(self):
        new_task = self.entry_task.get()
        if new_task:
            task_text = new_task
            task_var = tk.StringVar(value=task_text)

            # Checkbutton 
            check_button = tk.Checkbutton(self.task_display_frame, textvariable=task_var, font=("Helvetica", 12), bg="#FFB6C1", variable=tk.BooleanVar(), command=lambda: self.complete_task(task_var, check_button))
            check_button.grid(row=len(self.task_display_frame.winfo_children()), column=0, sticky="w")
            
            # Edit button
            edit_button = tk.Button(self.task_display_frame, text="Edit", command=lambda: self.edit_task(task_var), bg="#FF69B4", fg="black")
            edit_button.grid(row=len(self.task_display_frame.winfo_children()) - 1, column=1, padx=(0,5))

            # Delete button
            delete_button = tk.Button(self.task_display_frame, text="Delete", command=lambda: self.remove_task(task_var, check_button, edit_button, delete_button), bg="#FF69B4", fg="black")
            delete_button.grid(row=len(self.task_display_frame.winfo_children()) - 2, column=2, padx=(0,5))

            self.entry_task.delete(0, tk.END)  

            # Update task count
            self.task_count += 1
            self.update_task_count_label()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def edit_task(self, task_var):
        current_task = task_var.get()

        # Prompt user for the new task text
        new_task = simpledialog.askstring("Edit Task", "Enter new task:", initialvalue=current_task)

        if new_task:
            task_var.set(new_task)

    def complete_task(self, task_var, check_button):
        if " - Completed" not in task_var.get():
            task_var.set(f"{task_var.get()} - Completed")
            check_button.config(text=task_var.get(), font=("Helvetica", 12, "italic"), fg="gray")
            self.task_count -= 1
            self.update_task_count_label()
        else:
            task_var.set(task_var.get().replace(" - Completed", ""))
            check_button.config(text=task_var.get(), font=("Helvetica", 12), fg="black")

    def remove_task(self, task_var, check_button, edit_button, delete_button):
        check_button.destroy()
        edit_button.destroy()
        delete_button.destroy()

        self.task_count -= 1
        self.update_task_count_label()

    def update_task_count_label(self):
        self.task_count = max(0, self.task_count)  
        self.task_count_label.config(text=f"You have {self.task_count} {'task' if self.task_count == 1 else 'tasks'} to complete")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
