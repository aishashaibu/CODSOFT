import tkinter
import tkinter.messagebox 
import pickle 

root = tkinter.Tk()
root.title("Aisha's To-Do List")
           
def create_task():
    task = entry_task.get() 
    if task != "":
        listbox_task.insert(tkinter.END, task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning (title="warning!", message="Enter a task")
                                       
def save_task():
    tasks = listbox_task.get(0, listbox_task.size())
    pickle.dump(tasks, open("tasks.data", "wb"))
        
    
def update_task():
    listbox_task.curselection()
    if len(update_task)==0:
        tkinter.messagebox.showwarning("warning", "please select a task to update")

def track_tasks(): 
    try:
       tasks = pickle.track(open("tasks.data", "rb"))
       listbox_task.delete(0, tkinter.END, tasks)
       for task in tasks:
           listbox_task.insert(tkinter.END, task)
    except:
         tkinter.messagebox.showwarning (title="warning!", message="no tasks found.data.")

def delete_tasks():
    try:
       task_index = listbox_task.curselection()[0]
       listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="warning!", message="Select a task")

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()


listbox_task = tkinter.Listbox(frame_tasks, height=5, width=70, bg= "maroon", fg="white")
listbox_task.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

entry_task = tkinter.Entry(root, width=70)
entry_task.pack()

button_create_task = tkinter.Button(root, text= "Create task", width=68, command=create_task, bg="maroon", fg="white")
button_create_task.pack()

button_save_task= tkinter.Button(root, text= "Save task", width=68, command=save_task, bg="maroon", fg="white")
button_save_task.pack()

button_update_task= tkinter.Button(root, text= "update task", width=68, command=update_task, bg="maroon", fg="white")
button_update_task.pack()

button_track_task = tkinter.Button(root, text= "Track task", width=68, command=track_tasks, bg="maroon", fg="white")
button_track_task.pack()

button_delete_task = tkinter.Button(root, text= "Delete task", width=68, command=delete_tasks, bg="maroon", fg="white")
button_delete_task.pack()


root.mainloop()


