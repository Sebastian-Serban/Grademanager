import tkinter as tk
from grade import Grade


class Subject(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Notenrechner')
        self.geometry('963x750')
        self.resizable(False, False)

        self.header = tk.Frame(self)
        self.header.grid(columnspan=1, rowspan=2, ipadx=True)
        self.label = tk.Label(self.header, text='welcome to the grademanager', font=25)
        self.label.grid(column=0, row=0)



        # Buttons
        self.button_container = tk.Frame(self.header)
        self.button_container.grid(column=0, row=1)

        self.add_button = tk.Button(self.button_container, text='add grade')
        self.add_button['command'] = self.add
        self.add_button.grid(column=0, row=0)

        self.remove_button = tk.Button(self.button_container, text='remove grade')
        self.remove_button['command'] = self.remove
        self.remove_button.grid(column=1, row=0)

        self.result = tk.StringVar()
        self.average_label = tk.Label(self.button_container, text="average : ", font=20)
        self.average = tk.Label(self.button_container, textvariable=self.result, width=10, font=20, bg="white")
        self.average_label.grid(column=2, row=0)
        self.average.grid(column=3, row=0)

        #Grades container
        self.frame = tk.Frame(self)
        self.frame.grid(sticky="we")

        #Grades
        self.grades = []
        self.setup()

    def setup(self):
        for y in range(5):
            self.grades.append(Grade(self.frame, self))
            self.grades[-1].pack(fill="x")

    def add(self):
        self.grades.append(Grade(self.frame, self))
        self.grades[-1].pack()

    def remove(self):
        try:
            self.grades[-1].destroy()
            self.grades.pop(len(self.grades)-1)
            self.calc()
        except IndexError as error:
            print(error)

    def calc(self):
        grade_sum = 0
        weight_sum = 0
        for i in self.grades:
            try:
                if i.grade != "" and i.weight != "":
                    grade_sum += float(i.grade) * float(i.weight)
                    weight_sum += float(i.weight)
            except ValueError:
                continue
        if grade_sum and weight_sum:
            res = grade_sum / weight_sum
            res = 0.5 * round(res / 0.5)
            self.result.set(f"{res}")
        else:
            self.result.set(f"")


if __name__ == "__main__":
    root = Subject()
    root.mainloop()



