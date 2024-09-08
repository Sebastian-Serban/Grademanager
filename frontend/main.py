from login import Login
import json
import os


if __name__ == "__main__":
    try:
        with open("data.json", "r") as file:
            pass
    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump({}, file)

    app = Login()
    app.mainloop()
    os.remove("./data.json")



