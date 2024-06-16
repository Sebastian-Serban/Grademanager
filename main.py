import json
import tkinter as tk
from subject import Subject


class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Grade manager")
        self.geometry('863x760')
        self.resizable(False, False)

        self.header = tk.Frame(self)
        self.header.grid(columnspan=1, rowspan=2, pady=(0, 10))
        self.label = tk.Label(self.header, text="welcome to the grade manager", font='Helvetica 25')
        self.label.grid(column=0, row=0)

        # Buttons
        self.button_container = tk.Frame(self.header)
        self.button_container.grid(column=0, row=1)

        self.add_button = tk.Button(self.button_container, text='add subject')
        self.add_button['command'] = self.add
        self.add_button.grid(column=0, row=0)


        #Subjects container
        self.frame = tk.Frame(self)
        self.frame.grid(sticky="we")

        #Subjects
        self.subjects = []
        self.setup()

    def setup(self):
        with open("./data.json", 'r') as file:
            data = json.load(file)
            for y in data["subjects"]:
                self.subjects.append(SubjectContainer(self.frame, self, y["name"]))
                self.subjects[-1].pack()
                self.subjects[-1].weightvar.set(y["weight"])
                self.subjects[-1].gradevar.set(y["average"])
                self.subjects[-1].namevar.set(y["name"])
                self.subjects[-1].update()

    def add(self):
        top = tk.Toplevel(self)
        top.geometry("500x150")
        top.title("Add Subject")
        top.resizable(False, False)

        top.label = tk.Label(top, text="Add subject", font='Helvetica 15')
        top.label.pack(pady=10)

        top.header = tk.Frame(top)
        top.header.pack()

        top.name_label = tk.Label(top.header, text="Name", font='Helvetica 15')
        namevar = tk.StringVar(value="")
        top.name_field = tk.Entry(top.header, name="name", font='Helvetica 15', width=15, textvariable=namevar)
        top.name_label.grid(column=0, row=0)
        top.name_field.grid(column=1, row=0, padx=(10, 0))

        def save_and_close():
            name = namevar.get()
            if name:
                self.subjects.append(SubjectContainer(self.frame, self, name))
                self.subjects[-1].pack(fill="x")
                self.subjects[-1].update()
                top.destroy()

        top.submit_button = tk.Button(top, font='Helvetica 15', text="Save", command=save_and_close)
        top.submit_button.pack(side="bottom")


class SubjectContainer(tk.Frame):
    def __init__(self, parent, window, name):
        super().__init__(master=parent)
        self.weight = 0.0
        self.grade = 0.0
        self.name = name
        self.window = window

        self.id = tk.Label(self, text=f"{len(self.window.subjects) + 1}", font='Helvetica 15', width=6, relief="raised")
        self.id.grid(column=0, row=0, sticky="ns")

        self.name_container = tk.Frame(self, relief="raised", padx=10, bd=2)
        self.name_container.grid(column=1, row=0, sticky="ns")

        self.name_label = tk.Label(self.name_container, text="Subject", font='Helvetica 15')
        self.namevar = tk.StringVar(value=self.name)
        self.namevar.trace("w", self.update)
        self.name_field = tk.Entry(self.name_container, name="name", font='Helvetica 15', textvariable=self.namevar, state="readonly")
        self.name_field.config(readonlybackground="white")
        self.name_label.grid(column=0, row=0, padx=(0, 12))
        self.name_field.grid(column=1, row=0, padx=(0, 7))

        self.grade_container = tk.Frame(self, relief="raised", padx=10, bd=2)
        self.grade_container.grid(column=2, row=0, sticky="ns")

        self.grade_label = tk.Label(self.grade_container, text="Grade", font='Helvetica 15')
        self.gradevar = tk.StringVar(value="")
        self.gradevar.trace("w", self.update)
        self.grade_field = tk.Entry(self.grade_container, name="note", font='Helvetica 15', width=7,
                                    textvariable=self.gradevar, state="readonly")
        self.grade_field.config(readonlybackground="white")
        self.grade_label.grid(column=0, row=0, padx=(0, 12))
        self.grade_field.grid(column=1, row=0, padx=(0, 7))

        self.weight_container = tk.Frame(self, relief="raised", padx=10, bd=2)
        self.weight_container.grid(column=3, row=0, sticky="ns")

        self.weight_label = tk.Label(self.weight_container, text="Weight", font='Helvetica 15')
        self.weightvar = tk.StringVar(value="1.0")
        self.weightvar.trace("w", self.update)
        self.weight_field = tk.Entry(self.weight_container, name="weight", font='Helvetica 15', width=7,
                                     textvariable=self.weightvar)
        self.weight_label.grid(column=0, row=0, padx=(0, 12))
        self.weight_field.grid(column=1, row=0, padx=(0, 7))

        self.edit_button = tk.Button(self, text="✎", font='Helvetica 15', relief="raised",
                                     command=self.edit_subject)
        self.edit_button.grid(column=4, row=0)

        self.view_button = tk.Button(self, text="🔍", font='Helvetica 15', relief="raised",
                                     command=self.view_grades)
        self.view_button.grid(column=5, row=0)

    def update(self, *args):
        self.weight = self.weight_field.get()
        self.weight_field.config(bg="brown1" if not self.weight.replace(".", "").isnumeric() else "white")

    def view_grades(self):
        top = Subject(self.name)
        top.grab_set()

    def edit_subject(self):
        top = tk.Toplevel(self)
        top.geometry("500x150")
        top.title("Edit Subject")
        top.resizable(False, False)

        top.label = tk.Label(top, text="Edit Subject", font='Helvetica 15')
        top.label.pack(pady=10)

        top.header = tk.Frame(top)
        top.header.pack()

        top.name_label = tk.Label(top.header, text="Name", font='Helvetica 15')
        namevar = tk.StringVar(value=self.name if self.name else "")
        top.name_field = tk.Entry(top.header, name="name", font='Helvetica 15', width=15, textvariable=namevar)
        top.name_label.grid(column=0, row=0)
        top.name_field.grid(column=1, row=0, padx=(10, 0))

        def save_and_close():
            name = namevar.get()
            if name:
                self.name = name
                self.namevar.set(name)
                self.name_field.config(textvariable=self.namevar)
                top.destroy()

        def delete_and_close():
            self.window.subjects.pop(int(self.id.cget("text")) - 1)
            self.destroy()
            top.destroy()
            for i in self.window.subjects:
                i.id.config(text=f"{self.window.subjects.index(i)+1}")

        button_frame = tk.Frame(top)
        button_frame.pack(side="bottom", pady=10)

        top.submit_button = tk.Button(button_frame, font='Helvetica 15', text="Save", command=save_and_close)
        top.submit_button.grid(column=0, row=0, padx=(0, 10))

        top.delete_button = tk.Button(button_frame, font='Helvetica 15', text="Delete", command=delete_and_close)
        top.delete_button.grid(column=1, row=0, padx=(10, 0))


if __name__ == "__main__":
    root = Menu()
    root.mainloop()
