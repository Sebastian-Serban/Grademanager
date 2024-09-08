import tkinter as tk
from datetime import date


class Grade(tk.Frame):
    def __init__(self, parent, window):
        super().__init__(master=parent)
        self.window = window

        self.weight = "1.0"
        self.grade = ""
        self.name = ""
        self.date = date.today().strftime('%d.%m.%Y')

        self.id = tk.Label(self, text=f"{len(self.window.grades) + 1}", font='Helvetica 15', width=6, relief="raised")
        self.id.grid(column=0, row=0, sticky="ns")

        self.grade_container = tk.Frame(self, relief="raised", padx=10, bd=2)
        self.grade_container.grid(column=1, row=0)

        self.grade_label = tk.Label(self.grade_container, text="Grade", font='Helvetica 15')
        self.gradevar = tk.StringVar(value=self.grade)
        self.gradevar.trace("w", self.update)
        self.grade_field = tk.Entry(self.grade_container, name="note", font='Helvetica 15', width=7, textvariable=self.gradevar)
        self.grade_field.bind('<FocusIn>', highlight_text)
        self.grade_label.grid(column=0, row=0, padx=(0, 12))
        self.grade_field.grid(column=1, row=0, padx=(0, 7))

        self.weight_container = tk.Frame(self, relief="raised", padx=10, bd=2)
        self.weight_container.grid(column=2, row=0)

        self.weight_label = tk.Label(self.weight_container, text="Weight", font='Helvetica 15')
        self.weightvar = tk.StringVar(value=self.weight)
        self.weightvar.trace("w", self.update)
        self.weight_field = tk.Entry(self.weight_container, name="weight", font='Helvetica 15', width=7, textvariable=self.weightvar)
        self.weight_field.bind('<FocusIn>', highlight_text)
        self.weight_label.grid(column=0, row=0, padx=(0, 12))
        self.weight_field.grid(column=1, row=0, padx=(0, 7))

        self.date_container = tk.Frame(self, relief="raised", padx=10, bd=2)
        self.date_container.grid(column=3, row=0)

        self.date_label = tk.Label(self.date_container, text="Date", font='Helvetica 15')
        self.datevar = tk.StringVar(value=self.date)
        self.datevar.trace("w", self.update)
        self.date_field = tk.Entry(self.date_container, name="date", font='Helvetica 15', width=10, textvariable=self.datevar)
        self.date_field.bind('<FocusIn>', highlight_text)
        self.date_label.grid(column=0, row=0, padx=(0, 12))
        self.date_field.grid(column=1, row=0, padx=(0, 7))

        self.name_container = tk.Frame(self, relief="raised", padx=10, bd=2)
        self.name_container.grid(column=4, row=0, sticky="e")

        self.name_label = tk.Label(self.name_container, text="Title", font='Helvetica 15')
        self.namevar = tk.StringVar(value=self.name)
        self.namevar.trace("w", self.update)
        self.name_field = tk.Entry(self.name_container, name="name", font='Helvetica 15', textvariable=self.namevar)
        self.name_field.bind('<FocusIn>', highlight_text)
        self.name_label.grid(column=0, row=0, padx=(0, 12))
        self.name_field.grid(column=1, row=0, padx=(0, 7), sticky="e")

    def update(self, *args):
        self.weight = self.weight_field.get()
        self.grade = self.grade_field.get()
        self.name = self.name_field.get()
        self.date = self.date_field.get()

        self.weight_field.config(bg="brown1" if not self.weight.replace(".", "").isnumeric() else "white")
        self.grade_field.config(bg="brown1" if not self.grade.replace(".", "").isnumeric() and len(self.grade) else "white")

        self.window.calc()


def highlight_text(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
