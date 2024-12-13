from tkinter import *

class Gui:

    def __init__(self, window) -> None:
        """
        Initializes and creates a tkinter calculator gui window
        """

        self.window = window

        self.entry = StringVar()

        self.stat_entry = StringVar()

        entry_field = Entry(self.window, width=65,borderwidth=3,
                            state=DISABLED, textvariable=self.entry, justify='right')
        entry_field.grid(row=0, column=0, columnspan=5)

        self.stat_entry_field = Entry(self.window, width=65, borderwidth=3,
                                 state=DISABLED, textvariable=self.stat_entry, justify='right')

        self.error_label = Label(self.window, font='Helvetica 8')
        self.error_label.grid(row=2, column=3, columnspan=3)

        self.button_calc_mode = Button(self.window, text=f'CALC', padx=19, pady=20)

        self.button_1 = Button(self.window, text='1', padx=30, pady=20)
        self.button_2 = Button(self.window, text='2', padx=30, pady=20)
        self.button_3 = Button(self.window, text='3', padx=30, pady=20)
        self.button_4 = Button(self.window, text='4', padx=30, pady=20)
        self.button_5 = Button(self.window, text='5', padx=30, pady=20)
        self.button_6 = Button(self.window, text='6', padx=30, pady=20)
        self.button_7 = Button(self.window, text='7', padx=30, pady=20)
        self.button_8 = Button(self.window, text='8', padx=30, pady=20)
        self.button_9 = Button(self.window, text='9', padx=30, pady=20)
        self.button_0 = Button(self.window, text='0', padx=30, pady=20)

        self.button_decimal = Button(self.window, text='.', padx=32, pady=20)
        self.button_pm = Button(self.window, text='\u00B1', padx=29, pady=20)
        self.button_bp = Button(self.window, text='\u232B', padx=30, pady=20)
        self.button_clear = Button(self.window, text='C', padx=30, pady=20)

        # Calc Mode
        self.button_plus = Button(self.window, text='+', padx=33, pady=20)
        self.button_minus = Button(self.window, text='-', padx=32, pady=20)
        self.button_times = Button(self.window, text='*', padx=34, pady=20)
        self.button_div = Button(self.window, text='/', padx=32, pady=20)
        self.button_eq = Button(self.window, text='=', padx=76, pady=20)
        self.button_sin = Button(self.window, text='sin', padx=26, pady=20)
        self.button_cos = Button(self.window, text='cos', padx=29, pady=20)
        self.button_tan = Button(self.window, text='tan', padx=26, pady=20)
        self.button_trig = Button(self.window, text='DEG', padx=22, pady=20)

        # Stat Mode
        self.button_mean = Button(self.window, text='Mean', padx=23, pady=20)
        self.button_median = Button(self.window, text='Median', padx=14, pady=20)
        self.button_mode = Button(self.window, text='Mode', padx=22, pady=20)
        self.button_range = Button(self.window, text='Range', padx=18, pady=20)
        self.button_count = Button(self.window, text='Count', padx=17, pady=20)
        self.button_sum = Button(self.window, text='\u03A3', padx=30, pady=20)
        self.button_var = Button(self.window, text='Var', padx=29, pady=20)
        self.button_stdev = Button(self.window, text='\u03C3', padx=31, pady=20)
        self.button_comma = Button(self.window, text=',', padx=78, pady=20)

        # Grid Organization
        self.button_calc_mode.grid(row=3, column=0)
        self.button_trig.grid(row=3, column=1)
        self.button_sin.grid(row=3, column=2)
        self.button_cos.grid(row=3, column=3)
        self.button_tan.grid(row=3, column=4)

        self.button_7.grid(row=4, column=0)
        self.button_8.grid(row=4, column=1)
        self.button_9.grid(row=4, column=2)
        self.button_bp.grid(row=4, column=3)
        self.button_clear.grid(row=4, column=4)

        self.button_4.grid(row=5, column=0)
        self.button_5.grid(row=5, column=1)
        self.button_6.grid(row=5, column=2)
        self.button_times.grid(row=5, column=3)
        self.button_div.grid(row=5, column=4)

        self.button_1.grid(row=6, column=0)
        self.button_2.grid(row=6, column=1)
        self.button_3.grid(row=6, column=2)
        self.button_plus.grid(row=6, column=3)
        self.button_minus.grid(row=6, column=4)

        self.button_0.grid(row=7, column=0)
        self.button_decimal.grid(row=7, column=1)
        self.button_pm.grid(row=7, column=2)
        self.button_eq.grid(row=7, column=3, columnspan=2)


