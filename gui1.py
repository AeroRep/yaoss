from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import subprocess, traceback


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\\frame1")


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
    54.0,
    46.0,
    anchor="nw",
    text="Installing",
    fill="#FFFFFF",
    font=("Pretendard Variable Medium", 40 * -1)
)

canvas.create_text(
    56.0,
    96.0,
    anchor="nw",
    text="Installing Required Softwares...",
    fill="#FFFFFF",
    font=("Pretendard Variable Medium", 18 * -1)
)

canvas.create_rectangle(
    111.0,
    167.0,
    300.0,
    383.0,
    fill="#D9D9D9",
    outline="")
window.resizable(False, False)

try:
    subprocess.run("sudo pacman -Syu | pacman -Sy latte-dock | git clone https://github.com/aerorep/aero-de-conf -C /deconf | latte-dock --import-layout /deconf/aerodock.layout.latte | latte-dock")
    subprocess.run("python gui2.py")
    subprocess.run("pkill -9 yaoss")
except:
    messagebox.showerror("An error occurred", "Unexpected error occurred.\n" + traceback.format_exc())
    quit()

window.mainloop()   
