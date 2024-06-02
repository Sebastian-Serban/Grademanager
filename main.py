import tkinter as tk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Notenrechner')
        self.geometry('1000x1000')

        self.label = tk.Label(self, text='Willommen zum Notenrechner', font=25)
        self.frame = tk.Frame(self, bg="yellow")
        self.label.pack()
        self.frame.pack(fill="both", expand=True)


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
        super().__init__(master=parent)
        self.weight = 0.0
        self.grade = 0.0
        self.name = None
        self.date = None
        self.window = window
        self.window.add()

        self.id = tk.Label(self, text=f"{len(self.window.grades)+1}", font='Helvetica 15', height=3, width=6, relief="raised")
        self.id.grid(column=0, row=0)

        self.grade_container = tk.Frame(self, relief="raised", bg="red")
        self.grade_container.grid(column=1, row=0)

        self.label = tk.Label(self.grade_container, text=f"Note", font='Helvetica 15', height=2, bg="red")
        self.grade_field = tk.Entry(self.grade_container, name="note", font='Helvetica 15', width=10)
        self.label.grid(column=0, row=0)
        self.grade_field.grid(column=1, row=0)







if __name__ == "__main__":
    root = Window()
    root.mainloop()



