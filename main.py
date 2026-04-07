from typing import Tuple
from cryptography.fernet import Fernet
from github import Github, Auth
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import os, subprocess, sys, time, json
from pypresence.presence import Presence

os.chdir(os.path.abspath(os.path.dirname(__file__)))

ciper_suite = Fernet("jRbDavNPu-ssYiEdwYwG2OUMLEFJF4gQg6jFIIAGErY=")
decryptedtoken = ciper_suite.decrypt(
    "gAAAAABp1PJfeBR-O2jZKdTn6jlFQRWC9fx_RPF2cgWkBlA4T3wprVYqdDv7Qg6IaAxkA5X8YLhCuVmzZ_I3BEMsuodQNl3f-4GaOCiXVYH414yQqXelCaV-PuTFtVhvW30uhF-a6hUy"
).decode()
usabletoken = Auth.Token(decryptedtoken)
g = Github(auth=usabletoken)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Knockoff Roblox")
        self.RPC = Presence("1471592859554676999")
        self.RPC.connect()
        self.RPC.update(state="In Menu Screen", start=time.time())
        self.geometry("1200x800")
        self.gamesframe = ctk.CTkScrollableFrame(self, orientation="horizontal")
        self.gamesframe.pack(fill="both", expand=True)
        LoginPopup(self)
        for files in os.listdir("games"):
            if files.endswith(".py") and files != "__init__.py":
                text = files.removesuffix(".py")
                ctk.CTkButton(
                    self.gamesframe,
                    text=text,
                    font=("Arial", 50, "bold"),
                    command=lambda f=files: self.play_game(f),
                ).pack(side="left", padx=20)

    def play_game(self, game: str):
        text = game.removesuffix(".py")
        process = subprocess.Popen([sys.executable, f"games/{game}"])
        self.RPC.update(state=f"Playing {text} in Knockoff roblox", start=time.time())
        while process.poll() is None:
            time.sleep(1)
        self.RPC.update(state="In Menu Screen", start=time.time())


class LoginPopup(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__()
        self.title("Login or Signup")
        self.attributes(topmost=True)
        self.transient(master)
        self.grab_set()
        self.focus_set()
        ctk.CTkLabel(self, text="Username: ").grid(row=0, column=0)
        self.usernameentry = ctk.CTkEntry(self)
        self.usernameentry.grid(row=0, column=1)
        ctk.CTkLabel(self, text="Password: ").grid(row=1, column=0)
        self.passwordentry = ctk.CTkEntry(self, show="*")
        self.passwordentry.grid(row=1, column=1)
        self.signupbutton = ctk.CTkButton(self, text="Signup", command=self.signup)
        self.signupbutton.grid(row=2, column=0)
        self.loginbutton = ctk.CTkButton(self, text="Login", command=self.login)
        self.loginbutton.grid(row=2, column=1)

    def signup(self):
        username = ciper_suite.encrypt(self.usernameentry.get().encode()).decode()
        password = ciper_suite.encrypt(self.passwordentry.get().encode()).decode()
        template = {"username": username, "password": password}
        with open("logindetails.json", "w") as f:
            json.dump(template, fp=f, indent=2)

    def login(self):
        with open("logindetails.json", "r") as f:
            data = json.load(f)
        if (
            self.usernameentry.get() == ciper_suite.decrypt(data["username"]).decode()
            and self.passwordentry.get()
            == ciper_suite.decrypt(data["password"]).decode()
        ):
            self.destroy()
        else:
            CTkMessagebox(
                title="Login",
                message="Your username or password is incorrect",
                icon="cancel",
            )


if __name__ == "__main__":
    root = App()
    root.mainloop()
