# CTkCounterBox

A simple **unofficial** `customtkinter` widget to display and adjust a numeric counter using `+` and `–` buttons.  
Supports **floating-point steps**, **decimal formatting**, **value limiting**, and **signed/unsigned** counting.  
Fully resizable, styleable, and easy to integrate in any `customtkinter` GUI.
<img width="567" height="341" alt="Screenshot_1" src="https://github.com/user-attachments/assets/72e2cbbb-ffdf-427f-bccc-2bf14adc7312" />



> ❗ **Note:**  
> This widget is **not part of the official** [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter) library.  
---

## 📦 Installation

Clone or download the repo and place the `CTkCounterBox.py` file in the same directory as your project.

```bash
git clone https://github.com/xemilk/CTkCounterBox.git
```

Or just copy the CTkCounterBox.py into your project folder manually.

---

## Usage
```python
import customtkinter as ctk
from CTkCounterBox import CTkCounterBox

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x150")

counter = CTkCounterBox(app, start_value=0, step_width=1, decimals=0, signed=True, limit=20)
counter.pack(pady=20)```
```

# Access or modify value:
```python
print(counter.value)      # get current value
counter.value = 10        # set value
counter.step = 0.5        # change step size
counter.decimals = 2      # change decimal places

app.mainloop()
```
## Constructor Arguments
| Parameter     | Type    | Default  | Description                                                               |
| ------------- | ------- | -------- | ------------------------------------------------------------------------- |
| `master`      | widget  | required | Parent widget (e.g., `CTk`, `CTkFrame`)                                   |
| `start_value` | `float` | `0.0`    | Initial value of the counter                                              |
| `step_width`  | `float` | `1.0`    | Value to increment/decrement per click                                    |
| `signed`      | `bool`  | `True`   | If `True`, allows negative values                                         |
| `decimals`    | `int`   | `0`      | Number of decimal places to display                                       |
| `limit`       | `float` | `None`   | Max absolute value (e.g. ±10); works symmetrically if signed is `True`    |
| `button_size` | `int`   | `None`   | Size (width & height) of buttons and label (square); auto-sized if `None` |
| `**kwargs`    | `dict`  | –        | Additional keyword arguments passed to `CTkFrame`                         |

## Public Methods & Properties

| Name          | Description                                         |
| ------------- | --------------------------------------------------- |
| `value`       | Get or set the current counter value                |
| `step`        | Get or set the step size                            |
| `signed`      | Enable/disable negative values                      |
| `decimals`    | Get or set decimal precision                        |
| `limit`       | Get or set the absolute value limit                 |
| `.increase()` | Increases the value (respects `limit`)              |
| `.decrease()` | Decreases the value (respects `signed` and `limit`) |
