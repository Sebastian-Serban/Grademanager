import tkinter as tk
from subject import Subject


class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Grade manager")
        self.geometry('963x750')
        self.resizable(False, False)

        self.header = tk.Frame(self)
        self.header.grid(columnspan=1, rowspan=2)
        self.label = tk.Label(self.header, text="welcome to the grade manager", font=25)
        self.label.grid(column=0, row=0)

        # Buttons
        self.button_container = tk.Frame(self.header)
        self.button_container.grid(column=0, row=1)

        self.add_button = tk.Button(self.button_container, text='add subject')
        self.add_button['command'] = self.add
        self.add_button.grid(column=0, row=0)

        self.remove_button = tk.Button(self.button_container, text='remove subject')
        self.remove_button['command'] = self.remove
        self.remove_button.grid(column=1, row=0)

        #Subjects container
        self.frame = tk.Frame(self)
        self.frame.grid(sticky="we")

        #Subjects
        self.subjects = []
        self.setup()


    def add(self):
        return None

    def remove(self):
        return None

    def setup(self):
        for y in range(5):
            self.subjects.append(SubjectContainer(self.frame, self))
            self.subjects[-1].pack(fill="x")


class SubjectContainer(tk.Frame):
    def __init__(self, parent, window):
        super().__init__(master=parent)
        self.weight = 0.0
        self.grade = 0.0
        self.name = None
        self.window = window

        self.id = tk.Label(self, text=f"{len(self.window.subjects) + 1}", font='Helvetica 15', width=6, relief="raised")
        self.id.grid(column=0, row=0, sticky="ns")

        self.name_container = tk.Frame(self, relief="raised", padx=10, bd=2)
        self.name_container.grid(column=1, row=0)

        self.name_label = tk.Label(self.name_container, text="Subject", font='Helvetica 15')
        self.namevar = tk.StringVar(value="")
        self.namevar.trace("w", self.update)
        self.name_field = tk.Entry(self.name_container, name="name", font='Helvetica 15', textvariable=self.namevar, state="readonly")
        self.name_field.config(readonlybackground="white")
        self.name_label.grid(column=0, row=0, padx=(0, 12))
        self.name_field.grid(column=1, row=0, padx=(0, 7))

        self.grade_container = tk.Frame(self, relief="raised", padx=10, bd=2)
        self.grade_container.grid(column=2, row=0)

        self.grade_label = tk.Label(self.grade_container, text="Grade", font='Helvetica 15')
        self.gradevar = tk.StringVar(value="")
        self.gradevar.trace("w", self.update)
        self.grade_field = tk.Entry(self.grade_container, name="note", font='Helvetica 15', width=7,
                                    textvariable=self.gradevar)
        self.grade_label.grid(column=0, row=0, padx=(0, 12))
        self.grade_field.grid(column=1, row=0, padx=(0, 7))

        self.weight_container = tk.Frame(self, relief="raised", padx=10, bd=2)
        self.weight_container.grid(column=3, row=0)

        self.weight_label = tk.Label(self.weight_container, text="Weight", font='Helvetica 15')
        self.weightvar = tk.StringVar(value="1.0")
        self.weightvar.trace("w", self.update)
        self.weight_field = tk.Entry(self.weight_container, name="weight", font='Helvetica 15', width=7,
                                     textvariable=self.weightvar)
        self.weight_label.grid(column=0, row=0, padx=(0, 12))
        self.weight_field.grid(column=1, row=0, padx=(0, 7))


if __name__ == "__main__":
    root = Menu()
    root.mainloop()
