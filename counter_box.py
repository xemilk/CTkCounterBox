import customtkinter as ctk

class CounterBox(ctk.CTkFrame):
    """
    A CustomTkinter widget to display and adjust a numeric counter.
    Supports signed and unsigned values as well as floats with configurable decimal places.
    """

    def __init__(
        self,
        master=None,
        start_value=0.0,
        step_width=1.0,
        signed=True,
        decimals=0,
        button_size=None, 
        **kwargs
    ):
        """
        Initialize the CounterWidget.

        Args:
            master: Parent widget.
            start_value: Initial counter value (default 0.0).
            step_width: Step size for + and - buttons (default 1.0).
            signed: Allows negative values if True (default True).
            decimals: Number of decimal places shown (default 2).
            button_size: Width and height of buttons and label (square). 
                         If None, automatic based on font size.
            kwargs: Additional arguments for CTkFrame.
        """
        super().__init__(master, **kwargs)

        self._value = float(start_value)
        self._step = float(step_width)
        self._signed = signed
        self._decimals = max(0, decimals)

        # Determine button and label size
        if button_size is None:
            font = ctk.CTkLabel(master=self).cget("font")
            try:
                font_size = font[1]
            except Exception:
                font_size = 14
            self._button_size = font_size + 10
        else:
            self._button_size = button_size

        # Calculate font size as ~50% of button size, minimum 8
        self._font_size = max(8, int(self._button_size * 0.5))
        self._font = ("Arial", self._font_size)

        self._create_widgets()
        self._update_label()

    def _create_widgets(self):
        self._decrease_button = ctk.CTkButton(
            self,
            text="-",
            width=self._button_size,
            height=self._button_size,
            command=self.decrease,
            font=self._font
        )
        self._decrease_button.grid(row=0, column=0, padx=(0, 2))

        self._value_label = ctk.CTkLabel(
            self,
            width=self._button_size,
            height=self._button_size,
            anchor="center",
            justify="center",
            font=self._font
        )
        self._value_label.grid(row=0, column=1, padx=2)

        self._increase_button = ctk.CTkButton(
            self,
            text="+",
            width=self._button_size,
            height=self._button_size,
            command=self.increase,
            font=self._font
        )
        self._increase_button.grid(row=0, column=2, padx=(2, 0))

    def _format_value(self):
        format_string = f"{{:.{self._decimals}f}}"
        return format_string.format(self._value)

    def _update_label(self):
        self._value_label.configure(text=self._format_value())

    def increase(self):
        self._value += self._step
        self._update_label()

    def decrease(self):
        new_value = self._value - self._step
        if self._signed or new_value >= 0:
            self._value = new_value
            self._update_label()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if self._signed or new_value >= 0:
            self._value = float(new_value)
            self._update_label()

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, step_width):
        if step_width > 0:
            self._step = float(step_width)
        else:
            raise ValueError("Step width must be greater than 0")

    @property
    def signed(self):
        return self._signed

    @signed.setter
    def signed(self, allow_signed):
        self._signed = bool(allow_signed)

    @property
    def decimals(self):
        return self._decimals

    @decimals.setter
    def decimals(self, count):
        self._decimals = max(0, int(count))
        self._update_label()
