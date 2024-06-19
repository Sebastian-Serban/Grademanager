import tkinter as tk
from grade import Grade
import json


class Subject(tk.Toplevel):
    def __init__(self, name):
        super().__init__()
        self.weight = 0.0
        self.grade = 0.0
        self.name = name

        self.title(self.name)
        self.geometry('950x750')
        self.resizable(False, False)

        self.header = tk.Frame(self)
        self.header.grid(columnspan=1, rowspan=2, pady=(0, 10))
        self.label = tk.Label(self.header, text=self.name, font='Helvetica 25')
        self.label.grid(column=0, row=0)

        # Buttons
        self.button_container = tk.Frame(self.header)
        self.button_container.grid(column=0, row=1)

        self.add_button = tk.Button(self.button_container, text='Add Grade')
        self.add_button['command'] = self.add
        self.add_button.grid(column=0, row=0)

        self.remove_button = tk.Button(self.button_container, text='Remove Grade')
        self.remove_button['command'] = self.remove
        self.remove_button.grid(column=1, row=0)

        self.result = tk.StringVar()
        self.average_label = tk.Label(self.button_container, text="Average: ", font=20)
        self.average = tk.Label(self.button_container, textvariable=self.result, width=10, font=20, bg="white")
        self.average_label.grid(column=2, row=0)
        self.average.grid(column=3, row=0)

        # Grades container
        self.frame = tk.Frame(self)
        self.frame.grid(sticky="we")

        # Grades
        self.grades = []
        self.setup()

        # Save button
        self.save_button = tk.Button(self, text='Save', font='Helvetica 15', command=self.save)
        self.save_button.grid()

    def setup(self):
        with open("./data.json", 'r') as file:
            data = json.load(file)
            subject_index = [i for i in range(len(data["subjects"])) if data["subjects"][i]["name"] == self.name][0]
            if len(data["subjects"][subject_index]["grades"]) == 0:
                for y in range(5):
                    self.grades.append(Grade(self.frame, self))
                    self.grades[-1].pack(fill="x")
            else:
                for y in data["subjects"][subject_index]["grades"]:
                    self.grades.append(Grade(self.frame, self))
                    self.grades[-1].pack()
                    self.grades[-1].weightvar.set(y["weight"])
                    self.grades[-1].gradevar.set(y["grade"])
                    self.grades[-1].namevar.set(y["name"])
                    self.grades[-1].datevar.set(y["date"])
                    self.grades[-1].update()
                    self.calc()

    def add(self):
        self.grades.append(Grade(self.frame, self))
        self.grades[-1].pack()

    def remove(self):
        try:
            self.grades[-1].destroy()
            self.grades.pop(len(self.grades) - 1)
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
            self.grade = res
            self.result.set(f"{res}")
        else:
            self.result.set(f"")

    def save(self):
        with open("./data.json", 'r') as file:
            data = json.load(file)
            subject_index = [i for i in range(len(data["subjects"])) if data["subjects"][i]["name"] == self.name][0]
            data["subjects"][subject_index]["grades"] = []
            for i in self.grades:
                data["subjects"][subject_index]["grades"].append({"weight": i.weight_field.get(), "grade": i.grade_field.get(), "name": i.name_field.get(), "date": i.date_field.get()})
            data["subjects"][subject_index]["average"] = self.average["text"]
        with open("./data.json", 'w') as file:
            json.dump(data, file, indent=2)
        self.destroy()


def highlight_text(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')




