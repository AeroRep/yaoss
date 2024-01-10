from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import sys, subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def installDepend():
    subprocess.run("python gui2.py")
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
    56.0,
    46.0,
    anchor="nw",
    text="Installing",
    fill="#FFFFFF",
    font=("Pretendard Variable Medium", 40 * -1)
)

canvas.create_text(
    57.0,
    96.0,
    anchor="nw",
    text="Installing Required Softwares...",
    fill="#FFFFFF",
    font=("Pretendard Variable Medium", 18 * -1)
)

canvas.create_rectangle(
    203.0,
    214.0,
    211.0,
    311.0,
    fill="#3D96FF",
    outline="")
window.resizable(False, False)
window.mainloop()

installDepend()
