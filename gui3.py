
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import subprocess


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\sdbb2\OneDrive\바탕 화면\build\build\assets\frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class endPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent,bg="#151515")
        self.controller = controller

        canvas = Canvas(
            self,
            bg = "#151515",
            height = 493,
            width = 422,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            130.0,
            287.0,
            anchor="nw",
            text="That’s it!",
            fill="#FFFFFF",
            font=("Pretendard Variable Medium", 40 * -1)
        )

        canvas.create_text(
            60.0,
            336.0,
            anchor="nw",
            text="Begin your Aero Desktop Experience",
            fill="#FFFFFF",
            font=("Pretendard Variable Medium", 18 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: subprocess.run("restart -r now"),
            relief="flat"
        )
        button_1.place(
            x=127.0,
            y=395.0,
            width=167.0,
            height=42.0
        )

        canvas.create_text(
            165.0,
            145.0,
            anchor="nw",
            text="🎉",
            fill="#FFFFFF",
            font=("Pretendard Variable Medium", 96 * -1)
        )
