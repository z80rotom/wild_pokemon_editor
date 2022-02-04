from tkinter import *
from tkinter import ttk

class IVSpinbox(ttk.Spinbox):
    def __init__(self, master, textvariable):
        super().__init__(master, textvariable=textvariable, from_=0, to=31)
        self.configure(validate="key", validatecommand=(self.register(self.key_validate), '%P'))

    def key_validate(self, new_value):
        if not new_value.isdigit():
            return False
        minval = self.config('from')[4]
        maxval = self.config('to')[4]
        if int(new_value) not in range(minval, maxval+1):
            return False
        return True

class EVSpinbox(ttk.Spinbox):
    def __init__(self, master, textvariable):
        super().__init__(master, textvariable=textvariable, from_=0, to=252)
        self.configure(validate="key", validatecommand=(self.register(self.key_validate), '%P'))
    
    def key_validate(self, new_value):
        if not new_value.isdigit():
            return False
        minval = self.config('from')[4]
        maxval = self.config('to')[4]
        if int(new_value) not in range(minval, maxval+1):
            return False
        return True

class LevelSpinbox(ttk.Spinbox):
    def __init__(self, master, textvariable):
        super().__init__(master, textvariable=textvariable, from_=0, to=100)
        self.configure(validate="key", validatecommand=(self.register(self.key_validate), '%P'))

    def key_validate(self, new_value):
        if not new_value.isdigit():
            return False
        minval = self.config('from')[4]
        maxval = self.config('to')[4]
        if int(new_value) not in range(minval, maxval+1):
            return False
        return True

class EncRateSpinBox(ttk.Spinbox):
    def __init__(self, master, textvariable):
        super().__init__(master, textvariable=textvariable, from_=0, to=100)
        self.configure(validate="key", validatecommand=(self.register(self.key_validate), '%P'))

    def key_validate(self, new_value):
        if not new_value.isdigit():
            return False
        minval = self.config('from')[4]
        maxval = self.config('to')[4]
        if int(new_value) not in range(minval, maxval+1):
            return False
        return True