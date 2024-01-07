import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Welcome!")
app.geometry("640x480")

def button_function():
    print("button pressed")

pg_1_Title = ctk.CTkLabel(app, text="Welcome!", fg_color="transparent")
pg_1_subTitle = ctk.CTkLabel(app, text="Welcome to Aero Desktop.", fg_color="transparent")
pg_1_nextpgBtn = ctk.CTkButton(master=app, text="Get Started", command=button_function)

pg_1_Title.pack(padx=20, pady=20, anchor=ctk.CENTER)
pg_1_subTitle.pack(padx=20, pady=20, anchor=ctk.CENTER)
pg_1_nextpgBtn.place(relx=0.5, rely=0.75, anchor=ctk.CENTER)

app.mainloop()
