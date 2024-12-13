from gui import *
from math import sin, cos, tan, radians
from stats import mean, median, mode, range, variance, standard_deviation

expression: str = '0'
stat_result: float = 0
trig_mode: str = 'DEG'
calc_mode: str = 'CALC'
symbols: str  = ',.+-*/'

class Logic(Gui):

    def __init__(self, window) -> None:
        """
        Configures and controls the logic of a calculator gui window
        """

        super().__init__(window)

        self.button_calc_mode.config(command=self.switch_mode)

        self.button_1.config(command=lambda: self.button_press('1'))
        self.button_2.config(command=lambda: self.button_press('2'))
        self.button_3.config(command=lambda: self.button_press('3'))

        self.button_4.config(command=lambda: self.button_press('4'))
        self.button_5.config(command=lambda: self.button_press('5'))
        self.button_6.config(command=lambda: self.button_press('6'))

        self.button_7.config(command=lambda: self.button_press('7'))
        self.button_8.config(command=lambda: self.button_press('8'))
        self.button_9.config(command=lambda: self.button_press('9'))
        self.button_0.config(command=lambda: self.button_press('0'))

        self.button_decimal.config(command=lambda: self.button_press('.'))
        self.button_pm.config(command=self.negate)
        self.button_bp.config(command=self.backspace)
        self.button_clear.config(command=self.clear)

        # Calc Mode
        self.button_plus.config(command=lambda: self.button_press('+'))
        self.button_minus.config(command=lambda: self.button_press('-'))
        self.button_times.config(command=lambda: self.button_press('*'))
        self.button_div.config(command=lambda: self.button_press('/'))
        self.button_eq.config(command=self.evaluate)

        self.button_sin.config(command=lambda: self.trig_press(sin))
        self.button_cos.config(command=lambda: self.trig_press(cos))
        self.button_tan.config(command=lambda: self.trig_press(tan))

        self.button_trig.config(command=self.switch_trig)

        # Stat Mode
        self.button_mean.config(command=lambda: self.stat_press(mean))
        self.button_median.config(command=lambda: self.stat_press(median))
        self.button_mode.config(command=lambda: self.stat_press(mode))
        self.button_range.config(command=lambda: self.stat_press(range))
        self.button_comma.config(command=lambda: self.button_press(','))

        self.button_count.config(command=lambda: self.stat_press(len))
        self.button_sum.config(command=lambda: self.stat_press(sum))
        self.button_var.config(command=lambda: self.stat_press(variance))
        self.button_stdev.config(command=lambda: self.stat_press(standard_deviation))

        self.entry.set(expression)


    def switch_mode(self) -> None:
        """
        Switches the calculation mode from normal calculator mode
        to statistics mode, and vice versa.  When switching modes,
        buttons are also switched out and text on calc_mode button
        is toggled.
        """

        global calc_mode

        if calc_mode == 'CALC':
            self.switch_buttons()
            calc_mode = 'STAT'
            self.button_calc_mode.configure(text=f'{calc_mode}')
            self.clear()
            return

        self.switch_buttons()
        calc_mode = 'CALC'
        self.button_calc_mode.configure(text=f'{calc_mode}')
        self.clear()
        return


    def switch_trig(self) -> None:
        """
        Switches the trigonometry mode from degrees to radians,
        and vice versa.  Affects how the input of trigonometric
        functions (sin, cos, tan) are interpreted.  Toggles the
        text on trig_mode button.
        """

        global trig_mode

        if trig_mode == 'DEG':
            trig_mode = 'RAD'
            self.button_trig.configure(text=f'{trig_mode}')
            return

        trig_mode = 'DEG'
        self.button_trig.configure(text=f'{trig_mode}')


    def button_press(self, char: str) -> None:
        """
        This function handles any button press from the user.  The
        character added to the expression will change depending on
        which button the user presses.
        :param char: The character that will be added to the expression
        """

        global expression, symbols

        if char == '0' and len(expression) == expression.count('0'):
            return
        elif char in symbols and len(expression) == expression.count('0'):
            expression += char
            self.entry.set(expression)
            return
        elif len(expression) == expression.count('0'):
            expression = char
            self.entry.set(expression)
            return
        else:
            expression += char
            self.entry.set(expression)
            return


    def trig_press(self, function) -> None:
        """
        This function handles any button press that involves a trigonometric
        function (sin, cos, tan).  If trig_mode is in degrees, the input will
        first be converted to radians.  If trig_mode is in radians, the input
        will be unchanged.
        :param function: The function that will be executed for the result
        """

        global expression

        try:
            result = eval(expression)
            self.error_label.config(fg='black', text='')
        except:
            self.error_label.config(fg='red', text='Enter a valid expression')
            return

        if trig_mode == 'RAD':
            expression = str(function(result))
            self.entry.set(expression)
            return

        expression = str((function(radians(result))))
        self.entry.set(expression)


    def stat_press(self, function) -> None:
        """
        This function handles any button press that involves a function
        the stats module.  The input from the user is first converted from
        a string into a list of floats.  The executed function and the result
        are displayed in the stat_entry field.
        :param function: The function that will be executed for the result
        """

        global expression, stat_result

        elements = expression.split(',')

        data = [float(x) for x in elements]

        stat_result = function(data)

        if function == len:
            self.stat_entry.set(f'Count = {float(stat_result):.4f}')
            return

        self.stat_entry.set(f'{function.__name__.title()} = {float(stat_result):.4f}')
        return


    def clear(self) -> None:
        """
        Clears the global variable, expression, the primary entry_field,
        and the stat_entry_field.  Expression and entry_field are replaced
        by 0, while stat_entry_field is replaced by an empty string.
        """

        global expression
        expression = '0'
        self.entry.set(expression)
        self.stat_entry.set('')


    def backspace(self) -> None:
        """
        Deletes the character farthest to the right in the global
        variable, expression, and displays it onto the entry_field.
        If expression becomes an empty string from this operation,
        it is instead replaced by a 0.
        """

        global expression

        if not self.entry or len(expression) == expression.count('0'):
            return

        expression = expression[0:len(expression) - 1]

        if not expression:
            expression = '0'

        self.entry.set(expression)


    def negate(self) -> None:
        """
        Adds a negative sign to the beginning of the string, expression.  If the string
        is already negated, the negative sign is removed.  If the string only contains
        a singular 0, the function returns without changing the string.
        """

        global expression

        if expression[0] == '0':
            return

        if expression[0] == '-':
            expression = expression[1:len(expression)]
            self.entry.set(expression)
            return

        expression = '-' + expression
        self.entry.set(expression)


    def evaluate(self) -> None:
        """
        The expression string is evaluated using the eval() function and
        any errors are handled and shown to the user.
        """

        global expression

        try:
            expression = str(eval(expression))
            self.entry.set(expression)
            self.error_label.config(fg='black', text='')
        except ZeroDivisionError:
            self.error_label.config(fg='red', text='Cannot Divide by Zero')
        except:
            self.error_label.config(fg='red', text='Enter a valid expression')


    def forget_buttons(self) -> None:
        """
        Temporarily removes buttons depending on the calc_mode of the calculator.
        If the calculator is in normal calculator mode, arithmetic operators and
        trigonometric function buttons are removed.  Else, statistics function
        buttons are removed instead.
        """

        global calc_mode

        if calc_mode == 'CALC':
            self.button_plus.grid_forget()
            self.button_minus.grid_forget()
            self.button_times.grid_forget()
            self.button_div.grid_forget()

            self.button_trig.grid_forget()
            self.button_sin.grid_forget()
            self.button_cos.grid_forget()
            self.button_tan.grid_forget()

            self.button_eq.grid_forget()

            return

        self.button_mean.grid_forget()
        self.button_median.grid_forget()
        self.button_mode.grid_forget()
        self.button_range.grid_forget()

        self.button_count.grid_forget()
        self.button_sum.grid_forget()
        self.button_var.grid_forget()
        self.button_stdev.grid_forget()

        self.button_comma.grid_forget()

        self.stat_entry_field.grid_forget()

        return


    def remember_buttons(self) -> None:
        """
        Repacks buttons that have been temporarily removed from the calculator depending
        on the calc_mode of the calculator.  If the calculator is normal calculator mode,
        arithmetic operator and trigonometric function buttons are repacked.  Else, statistics
        function buttons are repacked instead.
        """

        global calc_mode

        if calc_mode == 'STAT':
            self.button_plus.grid(row=6, column=3)
            self.button_minus.grid(row=6, column=4)
            self.button_times.grid(row=5, column=3)
            self.button_div.grid(row=5, column=4)

            self.button_trig.grid(row=3, column=1)
            self.button_sin.grid(row=3, column=2)
            self.button_cos.grid(row=3, column=3)
            self.button_tan.grid(row=3, column=4)

            self.button_eq.grid(row=7, column=3, columnspan=2)

            return

        self.button_mean.grid(row=5, column=3)
        self.button_median.grid(row=5, column=4)
        self.button_mode.grid(row=6, column=3)
        self.button_range.grid(row=6, column=4)

        self.button_count.grid(row=3, column=1)
        self.button_sum.grid(row=3, column=2)
        self.button_var.grid(row=3, column=3)
        self.button_stdev.grid(row=3, column=4)

        self.button_comma.grid(row=7, column=3, columnspan=2)

        self.stat_entry_field.grid(row=1, column=0, columnspan=5)

        return


    def switch_buttons(self) -> None:
        """
        This function serves as a wrapper for the forget_buttons() and
        remember_buttons() functions, since they will always execute
        consecutively.
        """

        self.forget_buttons()
        self.remember_buttons()
        return