import customtkinter as ctk
import os, subprocess, sys, time
from pypresence.presence import Presence

os.chdir(os.path.abspath(os.path.dirname(__file__)))


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Knockoff Roblox")
        self.RPC = Presence("1471592859554676999")
        self.RPC.connect()
        self.RPC.update(start=time.time())
        self.geometry("1200x800")
        self.gamesframe = ctk.CTkScrollableFrame(self, orientation="horizontal")
        self.gamesframe.pack(fill="both", expand=True)
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
        subprocess.Popen([sys.executable, f"games/{game}"])
        self.RPC.update(state=f"Playing {text} in Knockoff roblox", start=time.time())


if __name__ == "__main__":
    root = App()
    root.mainloop()
