import tkinter as tk
import json
from tkinter import messagebox
from menu import Menu
import requests


class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry('900x600')
        self.minsize(800, 600)
        self.resizable(True, True)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)

        self.header = tk.Frame(self)
        self.header.grid(column=0, row=0, sticky="ew", pady=(0, 10))
        self.header.grid_columnconfigure(0, weight=1)

        self.label = tk.Label(self.header, text="Welcome to the Grade Manager", font='Helvetica 25')
        self.label.grid(column=0, row=0, pady=(10, 0))

        self.button_container = tk.Frame(self.header)
        self.button_container.grid(column=0, row=1, pady=(10, 10))
        self.button_container.grid_columnconfigure(0, weight=1)

        self.login_button = tk.Button(self.button_container, text='Login', font='Helvetica 15', command=self.show_login)
        self.login_button.pack(side="left", padx=10)

        self.register_button = tk.Button(self.button_container, text='Register', font='Helvetica 15',
                                         command=self.show_register)
        self.register_button.pack(side="right", padx=10)

        self.login_frame = None
        self.register_frame = None

    def show_login(self):
        if self.register_frame:
            self.register_frame.destroy()
        self.login_frame = tk.Frame(self)
        self.login_frame.grid(column=0, row=2, padx=20, pady=20)

        username_label = tk.Label(self.login_frame, text="Username:", font='Helvetica 15')
        username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_login_entry = tk.Entry(self.login_frame, font='Helvetica 15')
        self.username_login_entry.grid(row=0, column=1, padx=10, pady=10)

        password_label = tk.Label(self.login_frame, text="Password:", font='Helvetica 15')
        password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_login_entry = tk.Entry(self.login_frame, font='Helvetica 15', show="*")
        self.password_login_entry.grid(row=1, column=1, padx=10, pady=10)

        login_btn = tk.Button(self.login_frame, text="Login", font='Helvetica 15', command=self.login)
        login_btn.grid(row=2, column=0, columnspan=2, pady=10)

    def show_register(self):
        if self.login_frame:
            self.login_frame.destroy()
        self.register_frame = tk.Frame(self)
        self.register_frame.grid(column=0, row=2, padx=20, pady=20)

        username_label = tk.Label(self.register_frame, text="Username:", font='Helvetica 15')
        username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_register_entry = tk.Entry(self.register_frame, font='Helvetica 15')
        self.username_register_entry.grid(row=0, column=1, padx=10, pady=10)

        password_label = tk.Label(self.register_frame, text="Password:", font='Helvetica 15')
        password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_register_entry = tk.Entry(self.register_frame, font='Helvetica 15', show="*")
        self.password_register_entry.grid(row=1, column=1, padx=10, pady=10)

        register_btn = tk.Button(self.register_frame, text="Register", font='Helvetica 15', command=self.register)
        register_btn.grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_login_entry.get()
        password = self.password_login_entry.get()
        response = requests.get(f'http://localhost:5000/login/{username}/{password}')

        if response.json():
            with open('data.json', 'w') as json_file:
                json.dump(response.json()[0], json_file, indent=2)

            self.destroy()
            menu = Menu()
            menu.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def register(self):
        username = self.username_register_entry.get()
        password = self.password_register_entry.get()
        response = requests.post(f'http://localhost:5000/register/{username}/{password}')

        if not username or not password:
            messagebox.showerror("Registration Failed", "Both fields are required.")
            return
        else:
            if response.json():
                with open('data.json', 'w') as json_file:
                    json.dump({"subjects": []}, json_file, indent=2)

                self.destroy()
                menu = Menu()
                menu.mainloop()
            else:
                messagebox.showerror("Registration Failed", "Username already exists.")

