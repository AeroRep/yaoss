from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import traceback

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame2")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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
    text="Failed",
    fill="#FFFFFF",
    font=("Pretendard Variable Medium", 40 * -1)
)

canvas.create_text(
    56.0,
    96.0,
    anchor="nw",
    text=f"{traceback.format_exc()}",
    fill="#FFFFFF",
    font=("Pretendard Variable Medium", 18 * -1)
)

canvas.create_text(
    54.0,
    147.0,
    anchor="nw",
    text=f"{traceback.print_stack()}",
    fill="#FFFFFF",
    font=("Pretendard Variable Medium", 18 * -1)
)
window.resizable(False, False)
window.mainloop()
