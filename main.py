import tkinter as tk
from datetime import date

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Notenrechner')
        self.geometry('963x1000')
        self.resizable(False, False)

        self.label = tk.Label(self, text='Willommen zum Notenrechner', font=25)
        self.frame = tk.Frame(self, bg="yellow")
        self.label.pack()
        self.frame.pack(fill="x")


        #Buttons
        self.add_button = tk.Button(self, text='add grade')
        self.add_button['command'] = self.add
        self.add_button.pack()

        self.remove_button = tk.Button(self, text='remove grade')
        self.remove_button['command'] = self.remove
        self.remove_button.pack()

        #Grades
        self.grades = [tk.Label(self.frame, text=f'Note {i+1}', font=25, bg="purple") for i in range(5)]
        self.setup()
        self.grade = Grade(self.frame, self)
        self.grade.pack(fill="x")

    def setup(self):
        for y in self.grades:
            y.pack()

    def add(self):
        self.grades.append(tk.Label(self.frame, text=f'Note {len(self.grades)+1}', font=25, bg="purple"))
        self.grades[-1].pack()

    def remove(self):
        try:
            self.grades[-1].destroy()
            self.grades.pop(len(self.grades)-1)
        except IndexError as error:
            print(error)


class Grade(tk.Frame):
    def __init__(self, parent, window):
        super().__init__(master=parent, relief="raised", bg="blue")
        self.weight = 0.0
        self.grade = 0.0
        self.name = None
        self.date = date.today().strftime('%d.%m.%Y')
        self.window = window
        self.window.add()

        self.id = tk.Label(self, text=f"{len(self.window.grades) + 1}", font='Helvetica 15', width=6, relief="raised")
        self.id.grid(column=0, row=0, sticky="ns")

        self.grade_container = tk.Frame(self, relief="raised", padx=10, bd=2)
        self.grade_container.grid(column=1, row=0)

        self.grade_label = tk.Label(self.grade_container, text="Grade", font='Helvetica 15')
        self.gradevar = tk.StringVar(value="")
        self.gradevar.trace("w", self.update)
        self.grade_field = tk.Entry(self.grade_container, name="note", font='Helvetica 15', width=7, textvariable=self.gradevar)
        self.grade_label.grid(column=0, row=0, padx=(0, 12))
        self.grade_field.grid(column=1, row=0, padx=(0, 7))

        self.weight_container = tk.Frame(self, relief="raised", padx=10, bd=2)
        self.weight_container.grid(column=2, row=0)

        self.weight_label = tk.Label(self.weight_container, text="Weight", font='Helvetica 15')
        self.weightvar = tk.StringVar(value="1.0")
        self.weightvar.trace("w", self.update)
        self.weight_field = tk.Entry(self.weight_container, name="weight", font='Helvetica 15', width=7, textvariable=self.weightvar)
        self.weight_label.grid(column=0, row=0, padx=(0, 12))
        self.weight_field.grid(column=1, row=0, padx=(0, 7))

        self.date_container = tk.Frame(self, relief="raised", padx=10, bd=2)
        self.date_container.grid(column=3, row=0)

        self.date_label = tk.Label(self.date_container, text="Date", font='Helvetica 15')
        self.datevar = tk.StringVar(value=self.date)
        self.datevar.trace("w", self.update)
        self.date_field = tk.Entry(self.date_container, name="date", font='Helvetica 15', width=10, textvariable=self.datevar)
        self.date_label.grid(column=0, row=0, padx=(0, 12))
        self.date_field.grid(column=1, row=0, padx=(0, 7))

        self.name_container = tk.Frame(self, relief="raised", padx=10, bd=2)
        self.name_container.grid(column=4, row=0, sticky="e")

        self.name_label = tk.Label(self.name_container, text="Title", font='Helvetica 15')
        self.namevar = tk.StringVar(value="")
        self.namevar.trace("w", self.update)
        self.name_field = tk.Entry(self.name_container, name="name", font='Helvetica 15', textvariable=self.namevar)
        self.name_label.grid(column=0, row=0, padx=(0, 12))
        self.name_field.grid(column=1, row=0, padx=(0, 7), sticky="e")

    def update(self, *args):
        self.weight = self.weight_field.get()
        self.grade = self.grade_field.get()
        self.name = self.weight_field.get()
        self.date = self.date_field.get()










if __name__ == "__main__":
    root = Window()
    root.mainloop()



