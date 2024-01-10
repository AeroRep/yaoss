from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess, sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def cmd():
    subprocess.run("python gui1.py")
    sys.exit()

window = Tk()

window.geometry("422x493")
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
    126.0,
    287.0,
    anchor="nw",
    text="Welcome",
    fill="#FFFFFF",
    font=("Pretendard Variable Medium", 40 * -1)
)

canvas.create_text(
    125.0,
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
    command=lambda: cmd(),
    relief="flat"
)
button_1.place(
    x=127.0,
    y=395.0,
    width=167.0,
    height=42.0
)

emj_StartPage = PhotoImage(
    file=relative_to_assets(("Canvas.Image().png"))
)
emj_StartPageWave = canvas.create_image(
    200.0,
    190.0,
    image=emj_StartPage
)

window.resizable(False, False)
window.mainloop()
