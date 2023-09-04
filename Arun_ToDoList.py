from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from  tkinter import messagebox


def main():
    win = tk.Tk()
    app = Todolist(win)
    win.mainloop()

class Todolist:
    def __init__(self,root):
        self.root = root
        self.root.title('TO-DO-LIST')
        self.root.resizable(0,0)
        self.root.wm_iconbitmap('images/icon.ico')
        self.tasks = []
        self.done_tasks = set()

        # BACKGROUND IMG====
        img = Image.open('images/todo.jpg')
        imgsize = img.resize((600,700))
        self.imgbg = ImageTk.PhotoImage(imgsize)

        img_lbl = Label(self.root, image=self.imgbg)
        img_lbl.pack()

        # ADD BTN===
        addimg = Image.open('images/add.jpeg')
        addimgsize = addimg.resize((57, 57))
        self.addimgbg = ImageTk.PhotoImage(addimgsize)

        img_btn = Button(self.root, image=self.addimgbg,bg='white',border=0,command=self.add_task)
        img_btn.place(x=130, y=250)
        img_lbl = Button(self.root, text='ADD',bg='white',border=0,command=self.add_task)
        img_lbl.place(x=145, y=310)

        # UPDATE BTN ====
        Upimg = Image.open('images/update.jpg')
        Upimgsize = Upimg.resize((58, 58))
        self.Upimgbg = ImageTk.PhotoImage(Upimgsize)

        img_btn1 = Button(self.root, image=self.Upimgbg,bg='white',border=0,command=self.update_task)
        img_btn1.place(x=225, y=250)
        img_lbl1 = Button(self.root, text='Update', bg='white', border=0,command=self.update_task)
        img_lbl1.place(x=233, y=310)

        # DELETE BTN =====
        delimg = Image.open('images/delete.png')
        delimgsize = delimg.resize((54, 54))
        self.delimgbg = ImageTk.PhotoImage(delimgsize)

        img_btn2 = Button(self.root, image=self.delimgbg,bg='white',border=0,command=self.delete_task)
        img_btn2.place(x=320,y=250)
        img_lbl2 = Button(self.root, text='Delete', bg='white', border=0,command=self.delete_task)
        img_lbl2.place(x=330, y=310)

        # MARK AS DONE ====
        markimg = Image.open('images/mark.png')
        markimgsize = markimg.resize((54, 54))
        self.markimgbg = ImageTk.PhotoImage(markimgsize)

        img_btn3 = Button(self.root, image=self.markimgbg, bg='white', border=0, command=self.complete_task)
        img_btn3.place(x=413, y=250)
        img_lbl3 = Button(self.root, text='Mark', bg='white', border=0, command=self.complete_task)
        img_lbl3.place(x=425, y=310)

        # SAVE ====
        saveimg = Image.open('images/save.png')
        saveimgsize = saveimg.resize((75, 45))
        self.saveimgbg = ImageTk.PhotoImage(saveimgsize)

        img_btn4 = Button(self.root, image=self.saveimgbg, bg='white', border=0, command=self.save_tasks)
        img_btn4.place(x=420, y=565)

        self.entrybox = Entry(self.root, width=26,border=0,font=('Arial',18))
        self.entrybox.place(x=126,y=187,height=50)

        self.listbox = Listbox(self.root,width=25,border=0,background='white',font=('Arial Rounded MT Bold',18))
        self.listbox.place(x=125,y=373,height=177)

        self.listbox.bind("<Double-1>", self.edit_task)

        # FUNCTIONS======================

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    self.listbox.insert(tk.END, line.strip())
        except FileNotFoundError:
            pass

    def add_task(self):
        task = self.entrybox.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.entrybox.delete(0, tk.END)
        else:
            tk.messagebox.showwarning("Warning", "Task cannot be empty!")

    def update_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            updated_task = self.entrybox.get()
            if updated_task:
                self.tasks[selected_task_index] = updated_task
                self.update_task_listbox()
                self.entrybox.delete(0, tk.END)
        elif self.entrybox.get() == '':
            messagebox.showinfo('To-Do-List','Please select a task to update', parent=self.root)

    def edit_task(self, event):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            selected_task = self.tasks[selected_task_index]
            self.entrybox.delete(0, tk.END)
            self.entrybox.insert(0, selected_task)

    def delete_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            del self.tasks[selected_index]
            self.update_task_listbox()

    def complete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            task = self.tasks[selected_task_index]
            task = "✔ " + task if not task.startswith("✔ ") else task[2:]
            self.tasks[selected_task_index] = task
            self.listbox.itemconfig(selected_task_index, {'bg': 'light green'})
            self.done_tasks.add(selected_task_index)
            self.save_tasks()
            self.update_task_listbox()

    def save_tasks(self):
        tasks = self.listbox.get(0, tk.END)
        with open("tasks.txt", "w") as file:
            for i, task in enumerate(tasks):
                task = task.strip()
                if i in self.done_tasks:
                    task = f"[DONE] {task}"
                file.write(task + "\n")

    def update_task_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__=='__main__':
     main()


