from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, Frame
import traceback, app, gui1

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\\frame0")

class mainStartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent,bg="#151515")
        self.controller = controller

        try:
            def relative_to_assets(path: str) -> Path:
                return ASSETS_PATH / Path(path)


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
                command=lambda: app.APP.show_frame(gui1),
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
            self.resizable(False, False)
            self.mainloop()
        except:
            messagebox.showerror("An error occurred", "Unexpected error occurred.\n" + traceback.format_exc())
            quit()