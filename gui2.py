from pathlib import Path

from tkinter import Tk, Canvas, Text, Button, PhotoImage, Frame
import gui3, app

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class setModePage(Frame):
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
            50.0,
            46.0,
            anchor="nw",
            text="Customize",
            fill="#FFFFFF",
            font=("Pretendard Variable Medium", 40 * -1)
        )

        canvas.create_text(
            54.0,
            96.0,
            anchor="nw",
            text="Customize your Aero",
            fill="#FFFFFF",
            font=("Pretendard Variable Medium", 18 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("light mode"),
            relief="flat"
        )
        button_1.place(
            x=42.0,
            y=247.0,
            width=168.0,
            height=130.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: app.show_frame(gui3),
            relief="flat"
        )
        button_2.place(
            x=317.0,
            y=430.0,
            width=78.0,
            height=42.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("dark mode"),
            relief="flat"
        )
        button_3.place(
            x=211.0,
            y=247.0,
            width=168.0,
            height=130.0
        )
