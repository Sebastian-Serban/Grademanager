from subject import Subject
import tkinter as tk
import json


class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Grade Manager")
        self.geometry('900x900')
        self.minsize(800, 700)
        self.resizable(True, True)

        # Configure grid to make it scalable
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)

        # Header Frame
        self.header = tk.Frame(self)
        self.header.grid(column=0, row=0, sticky="ew", pady=(0, 10))
        self.header.grid_columnconfigure(0, weight=1)

        # Title Label
        self.label = tk.Label(self.header, text="Welcome to the Grade Manager", font='Helvetica 25')
        self.label.grid(column=0, row=0, pady=(10, 0))

        # Buttons Container Frame
        self.button_container = tk.Frame(self.header)
        self.button_container.grid(column=0, row=1, pady=(10, 10))
        self.button_container.grid_columnconfigure(0, weight=1)

        # Add Subject Button
        self.add_button = tk.Button(self.button_container, text='Add Subject', font='Helvetica 15')
        self.add_button['command'] = self.add
        self.add_button.pack(fill='x', expand=True)

        # Subject container
        self.canvas = tk.Canvas(self)
        self.canvas.grid(column=0, row=2, sticky="nsew")

        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(column=1, row=2, sticky="ns")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollable_frame = tk.Frame(self.canvas)

        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.scrollable_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind('<Configure>', self.on_canvas_configure)

        # Subjects list
        self.subjects = []
        self.setup()

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)

    def setup(self):
        with open("./data.json", 'r') as file:
            data = json.load(file)
            for y in data["subjects"]:
                subject_container = SubjectContainer(self.scrollable_frame, self, y["name"])
                subject_container.pack(fill='x')
                subject_container.weightvar.set(y["weight"])
                subject_container.gradevar.set(y["average"])
                subject_container.namevar.set(y["name"])
                subject_container.update()
                self.subjects.append(subject_container)

    def add(self):
        top = tk.Toplevel(self)
        top.geometry("500x150")
        top.title("Add Subject")
        top.resizable(True, True)

        top.grid_columnconfigure(0, weight=1)
        top.grid_rowconfigure(0, weight=0)
        top.grid_rowconfigure(1, weight=1)

        top.label = tk.Label(top, text="Add Subject", font='Helvetica 15')
        top.label.grid(row=0, column=0, pady=10)

        top.header = tk.Frame(top)
        top.header.grid(row=1, column=0)
        top.header.grid_columnconfigure(0, weight=1)

        top.name_label = tk.Label(top.header, text="Name", font='Helvetica 15')
        namevar = tk.StringVar(value="")
        top.name_field = tk.Entry(top.header, font='Helvetica 15', width=15, textvariable=namevar)
        top.name_label.grid(column=0, row=0, sticky="e")
        top.name_field.grid(column=1, row=0, padx=(10, 0))

        def save_and_close():
            name = namevar.get()
            if name:
                with open("./data.json", 'r') as file:
                    data = json.load(file)
                    data["subjects"].append({"weight": "1.0", "name": name, "average": "", "grades": []})

                with open("./data.json", 'w') as file:
                    json.dump(data, file, indent=2)

                subject_container = SubjectContainer(self.scrollable_frame, self, name)
                subject_container.pack(fill='x')
                self.subjects.append(subject_container)
                top.destroy()

        top.submit_button = tk.Button(top, font='Helvetica 15', text="Save", command=save_and_close)
        top.submit_button.grid(row=2, column=0, pady=(10, 0))


class SubjectContainer(tk.Frame):
    def __init__(self, parent, window, name):
        super().__init__(master=parent)
        self.weight = 0.0
        self.grade = 0.0
        self.name = name
        self.window = window

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)

        self.id = tk.Label(self, text=f"{len(self.window.subjects) + 1}", font='Helvetica 15', width=6, relief="raised")
        self.id.grid(column=0, row=0, sticky="nsew")

        self.name_container = tk.Frame(self, relief="raised", padx=10, bd=2)
        self.name_container.grid(column=1, row=0, sticky="nsew")

        self.name_label = tk.Label(self.name_container, text="Subject", font='Helvetica 15')
        self.namevar = tk.StringVar(value=self.name)
        self.namevar.trace("w", self.update)
        self.name_field = tk.Entry(self.name_container, name="name", font='Helvetica 15', textvariable=self.namevar, state="readonly")
        self.name_field.config(readonlybackground="white")
        self.name_label.grid(column=0, row=0, padx=(0, 12))
        self.name_field.grid(column=1, row=0, padx=(0, 7))

        self.grade_container = tk.Frame(self, relief="raised", padx=10, bd=2)
        self.grade_container.grid(column=2, row=0, sticky="nsew")

        self.grade_label = tk.Label(self.grade_container, text="Grade", font='Helvetica 15')
        self.gradevar = tk.StringVar(value="")
        self.gradevar.trace("w", self.update)
        self.grade_field = tk.Entry(self.grade_container, name="note", font='Helvetica 15', width=7, textvariable=self.gradevar, state="readonly")
        self.grade_field.config(readonlybackground="white")
        self.grade_label.grid(column=0, row=0, padx=(0, 12))
        self.grade_field.grid(column=1, row=0, padx=(0, 7))

        self.weight_container = tk.Frame(self, relief="raised", padx=10, bd=2)
        self.weight_container.grid(column=3, row=0, sticky="nsew")

        self.weight_label = tk.Label(self.weight_container, text="Weight", font='Helvetica 15')
        self.weightvar = tk.StringVar(value="1.0")
        self.weightvar.trace("w", self.update)
        self.weight_field = tk.Entry(self.weight_container, name="weight", font='Helvetica 15', width=7, textvariable=self.weightvar)
        self.weight_field.bind('<FocusIn>', highlight_text)
        self.weight_label.grid(column=0, row=0, padx=(0, 12))
        self.weight_field.grid(column=1, row=0, padx=(0, 7))

        self.edit_button = tk.Button(self, text="✎", font='Helvetica 15', relief="raised", command=self.edit_subject)
        self.edit_button.grid(column=4, row=0, sticky="nsew")

        self.view_button = tk.Button(self, text="🔍", font='Helvetica 15', relief="raised", command=self.view_grades)
        self.view_button.grid(column=5, row=0, sticky="nsew")

    def update(self, *args):
        self.weight = self.weight_field.get()
        self.weight_field.config(bg="brown1" if not self.weight.replace(".", "").isnumeric() else "white")

    def view_grades(self):
        top = Subject(self.name)
        top.grab_set()
        self.window.wait_window(top)
        with open("./data.json", 'r') as file:
            data = json.load(file)
            self.gradevar.set(data["subjects"][int(self.id.cget("text")) - 1]["average"])

    def edit_subject(self):
        top = tk.Toplevel(self)
        top.geometry("500x150")
        top.title("Edit Subject")
        top.resizable(True, True)

        top.grid_columnconfigure(0, weight=1)
        top.grid_rowconfigure(0, weight=1)
        top.grid_rowconfigure(1, weight=1)

        top.label = tk.Label(top, text="Edit Subject", font='Helvetica 15')
        top.label.grid(row=0, column=0, pady=10, sticky="n")

        top.header = tk.Frame(top)
        top.header.grid(row=1, column=0)

        top.name_label = tk.Label(top.header, text="Name", font='Helvetica 15')
        namevar = tk.StringVar(value=self.name if self.name else "")
        top.name_field = tk.Entry(top.header, name="name", font='Helvetica 15', width=15, textvariable=namevar)
        top.name_field.bind('<FocusIn>', highlight_text)
        top.name_label.grid(column=0, row=0, sticky="n")
        top.name_field.grid(column=1, row=0, padx=(10, 0), sticky="w")

        def save_and_close():
            name = namevar.get()
            if name:
                with open("./data.json", 'r') as file:
                    data = json.load(file)
                    data["subjects"][int(self.id.cget("text")) - 1]["name"] = name

                with open("./data.json", 'w') as file:
                    json.dump(data, file, indent=2)

                self.name = name
                self.namevar.set(name)
                self.name_field.config(textvariable=self.namevar)
                top.destroy()

        def delete_and_close():
            with open("./data.json", 'r') as file:
                data = json.load(file)
                data["subjects"].pop(int(self.id.cget("text")) - 1)

            with open("./data.json", 'w') as file:
                json.dump(data, file, indent=2)

            self.window.subjects.pop(int(self.id.cget("text")) - 1)
            self.destroy()
            top.destroy()
            for i in self.window.subjects:
                i.id.config(text=f"{self.window.subjects.index(i)+1}")

        button_frame = tk.Frame(top)
        button_frame.grid(row=2, column=0, pady=10)
        button_frame.grid_columnconfigure(0, weight=1)

        top.submit_button = tk.Button(button_frame, font='Helvetica 15', text="Save", command=save_and_close)
        top.submit_button.grid(column=0, row=0, padx=(0, 10), sticky="e")

        top.delete_button = tk.Button(button_frame, font='Helvetica 15', text="Delete", command=delete_and_close)
        top.delete_button.grid(column=1, row=0, padx=(10, 0), sticky="w")


def highlight_text(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')