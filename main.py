import customtkinter as ctk
from counter_box import CounterBox

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("CustomTkinter Counter Widget")
app.geometry("300x150")

counter = CounterBox(app)
counter.pack(pady=40)

app.mainloop()
