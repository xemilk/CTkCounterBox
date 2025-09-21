import customtkinter as ctk
from CTkCounterBox import CTkCounterBox

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x150")

counter = CTkCounterBox(app, start_value=0, step_width=1, decimals=0, signed=True, limit=20)
counter.pack(pady=20)

# Access or modify value:
print(counter.value)      # get current value
counter.value = 10        # set value
counter.step = 0.5        # change step size
counter.decimals = 2      # change decimal places

app.mainloop()
