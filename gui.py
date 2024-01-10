from pathlib import Path

# from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import subprocess, os, traceback

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\\frame0")

try:
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("422x493")
    window.title("yaoss")
    window.configure(bg = "#151515")


    canvas = Canvas(
        window,
        bg = "#151515",
        height = 493,
        width = 422,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        127.0,
        287.0,
        anchor="nw",
        text="Welcome",
        fill="#FFFFFF",
        font=("Pretendard Variable Medium", 40 * -1)
    )

    canvas.create_text(
        123.5,
        336.0,
        anchor="nw",
        text="Get Started from here",
        fill="#FFFFFF",
        font=("Pretendard Variable Medium", 18 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: subprocess.run("python " + os.getcwd() + "\\gui1.py | pkill -9 yaoss"),
        relief="flat",
        bd=0
    )
    button_1.place(
        x=127.0,
        y=395.0,
        width=167.0,
        height=42.0
    )

    canvas.create_text(
        145.0,
        145.0,
        anchor="nw",
        text="👋",
        fill="#FFFFFF",
        font=("Pretendard Variable Medium", 96 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
except:
    messagebox.showerror("An error occurred", "Unexpected error occurred.\n" + traceback.format_exc())
    quit()