# Imports the tkinter library and is assigned the shortcut tk for easier access
import tkinter as tk
# Imports the messagebox module from tkinter for displaying warning message boxes
from tkinter import Label, messagebox, Text

class ToDoListApp:
    # The class's constructor method. It initializes the application's primary components.
    def __init__(self, root):

        #  Creates a frame widget to hold other widgets.
        self.root = root
        # Giving the title to our Application
        self.root.title("To-Do App")
        self.completed_tasks = 0

        intro_label = Label(root, text="Organize Your Day With Ease!")
        intro_label.configure(background = "orange")
        intro_label.config(font=('Comic Sans MS', 15), fg = "white")
    
        manual_label_1 = Label(root, text = "Write down the task you want, and then click add task to add it on your list ->")
        manual_label_2 = Label(root, text = "After completing your task, you can mark it as completed!")
        manual_label_3 = Label(root, text = f"You can delete the tasks by clicking the RED DELETE TASK button")
        
        # Displaying the labels on the UI 
        intro_label.pack()
        manual_label_1.pack()
        manual_label_2.pack()
        manual_label_3.pack()

        #Re-coloring the labels backgrounds to orange
        manual_label_1.configure(background = "orange")
        manual_label_2.configure(background = "orange")
        manual_label_3.configure(background = "orange")
    
        # Initializes an empty list to store tasks.
        self.tasks = []

        # Creates a frame widget to hold other widgets.
        self.frame = tk.Frame(root)
        # Packs the frame into the window with a vertical padding of 10 pixels.
        self.frame.pack(pady=30)

        # Creates an entry box for task input with a width of 30 characters.
        self.task_entry = tk.Entry(self.frame, width=30)
        # Places the entry widget in the grid layout at row 0, column 0 with a horizontal padding of 10 pixels.
        self.task_entry.grid(row=0, column=0, padx=10)

        #Creating the buttons
        #Creates a button labeled "Add Task" that calls the add_task method when clicked.
        self.add_task_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        # Places the button in the grid layout at row 0, column 1.
        self.add_task_button.grid(row=0, column=1)
        

        # Creates a list box widget to display tasks with a width of 50 characters and a height of 15 rows, allowing single selection.
        self.task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        # Packs the listbox into the window with a vertical padding of 10 pixels.
        self.task_listbox.pack(pady=10)

        # Other buttons
        self.completed_label = Label(root, text=f"Completed Tasks: {self.completed_tasks}")
        self.completed_label.pack(pady=10) 
        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)
        self.mark_completed_button = tk.Button(root, text="Mark as Completed", command=self.mark_task_completed)
        self.mark_completed_button.pack(pady=5)
        self.change_task_task_button = tk.Button(root, text = "Change Task", command=self.change_task)
        self.change_task_task_button.pack(pady= 10)
        
        
        #Re-coloring the buttons
        self.delete_task_button.configure(background = "red", fg = "white")
        self.completed_label.configure(background='orange', font=('Comic Sans MS', 12), fg="white")
        self.mark_completed_button.configure(background = "green", fg = "white")
        self.add_task_button.configure(background="yellow")
        self.change_task_task_button.configure(background="yellow")

        # Sets the background of the root to orange 
        root.configure(background='orange')

        # Calls the reset_listbox method to update the listbox with the current tasks.
        self.reset_listbox()


    #Adding a task method:
    def add_task(self):
        # Get the task from the entry widget
        task = self.task_entry.get()
        # Check if the task is not empty
        if task:
            # Add the task to the task list with a 'completed' status of False
            self.tasks.append({"task": task, "completed": False})
            # Clear the entry widget
            self.task_entry.delete(0, tk.END)
            # Refresh the listbox to show the updated list of tasks
            self.reset_listbox()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def change_task(self):
        selected_task_index = self.task_listbox.curselection()

        if selected_task_index:
            task_index = selected_task_index[0]
            # Get the new task description from the entry widget
            new_task = self.task_entry.get()
        if new_task:
            # Update the task description in the task list
            self.tasks[task_index]["task"] = new_task
            self.task_entry.delete(0, tk.END)
            # Refresh the listbox to show the updated list of tasks
            self.reset_listbox()
        else:
            messagebox.showwarning("Warning", "You must enter a new task.")
       

    def delete_task(self):
            selected_task_index = self.task_listbox.curselection()
        # Check if a task is selected
            if selected_task_index:
            # Get the index of the selected task
                task_index = selected_task_index[0]
            # Delete the task from the task list
                del self.tasks[task_index]
            # Refresh the listbox to show the updated list of tasks
                self.reset_listbox()
            else:
                messagebox.showwarning("Warning", "You must select a task to delete.")

    def mark_task_completed(self):
    # Get the selected task index from the listbox
        selected_task_index = self.task_listbox.curselection()
        # Check if a task is selected
        if selected_task_index:
            # Get the index of the selected task
            task_index = selected_task_index[0]
            # Mark the task as completed in the task list
            self.tasks[task_index]["completed"] = True
            # Refresh the listbox to show the updated list of tasks
            self.reset_listbox()
            self.completed_tasks += 1
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

   # Refresh the listbox method:
    def reset_listbox(self):
        # Delete all items from the listbox
        self.task_listbox.delete(0, tk.END)
        # Reset completed tasks count
        self.completed_tasks = 0
        # Iterate over the task list
        for task in self.tasks:
            # Set the status based on the 'completed' flag
            status = "COMPLETED" if task["completed"] else "Not Completed"
            # Insert the task and its status into the listbox
            self.task_listbox.insert(tk.END, f"{task['task']} - {status}")
            # Increment the completed tasks count if the task is completed
            if task["completed"]:
                self.completed_tasks += 1
        
        self.completed_label.config(text=f"Completed Tasks: {self.completed_tasks}")
    
    

def main():    
    # Create the main application window
    root = tk.Tk()
    
    # Create an instance of the ToDoListApp class and pass the root window to it
    app = ToDoListApp(root)
    
    # Start the Tkinter event loop
    root.mainloop()

# If this script is being run directly (and not imported as a module), execute the main function
if __name__ == "__main__":
    main()
