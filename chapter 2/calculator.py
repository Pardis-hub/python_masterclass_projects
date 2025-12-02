# imports
import tkinter as tk

# Calculator class
class Calculator():
    def __init__(self):
        self.expr = ""
        self.window = tk.Tk()
        self.window.title("Python Calculator")
        self.window.resizable(width= False, height= False)
        self.window.geometry("400x230")

        # display entry
        self.display = tk.StringVar()
        self.display_entry = tk.Entry(self.window, textvariable= self.display, bd=5, font = ('calibre',20))
        self.display_entry.grid(row= 0, column= 0, columnspan=4, pady= 10)
        # buttons
        tk.Button(self.window, text= "7", width= 13, height= 2, command= lambda: self.press(7)).grid(row=1, column=0, sticky=tk.W+tk.E)
        tk.Button(self.window, text= "8", width= 13, height= 2, command= lambda: self.press(8)).grid(row=1, column=1, sticky=tk.W+tk.E)
        tk.Button(self.window, text= "9", width= 13, height= 2, command= lambda: self.press(9)).grid(row=1, column=2, sticky=tk.W+tk.E)
        tk.Button(self.window, text= "+", width= 13, height= 2, command= lambda: self.press('+')).grid(row=1, column=3, sticky=tk.W+tk.E)
        tk.Button(self.window, text= "4", width= 13, height= 2, command= lambda: self.press(4)).grid(row=2, column=0, sticky=tk.W+tk.E)
        tk.Button(self.window, text= "5", width= 13, height= 2, command= lambda: self.press(5)).grid(row=2, column=1, sticky=tk.W+tk.E)
        tk.Button(self.window, text= "6", width= 13, height= 2, command= lambda: self.press(6)).grid(row=2, column=2, sticky=tk.W+tk.E)
        tk.Button(self.window, text= "-", width= 13, height= 2, command= lambda: self.press('-')).grid(row=2, column=3, sticky=tk.W+tk.E)
        tk.Button(self.window, text= "1", width= 13, height= 2, command= lambda: self.press(1)).grid(row=3, column=0, sticky=tk.W+tk.E)
        tk.Button(self.window, text= "2", width= 13, height= 2, command= lambda: self.press(2)).grid(row=3, column=1, sticky=tk.W+tk.E)
        tk.Button(self.window, text= "3", width= 13, height= 2, command= lambda: self.press(3)).grid(row=3, column=2, sticky=tk.W+tk.E)
        tk.Button(self.window, text= "*", width= 13, height= 2, command= lambda: self.press('*')).grid(row=3, column=3, sticky=tk.W+tk.E)
        tk.Button(self.window, text= "C", width= 13, height= 2, command= self.clear_display).grid(row=4, column=0, sticky=tk.W+tk.E)
        tk.Button(self.window, text= "0", width= 13, height= 2, command= lambda: self.press(0)).grid(row=4, column=1, sticky=tk.W+tk.E)
        tk.Button(self.window, text= "=", width= 13, height= 2, command= self.detect_action).grid(row=4, column=2, sticky=tk.W+tk.E)
        tk.Button(self.window, text= "/", width= 13, height= 2, command= lambda: self.press('/')).grid(row=4, column=3, sticky=tk.W+tk.E)


    def add(self, nums):
        return float(nums[0]) + float(nums[1])

    def subtract(self, nums):
        return float(nums[0]) - float(nums[1])

    def multiply(self, nums):
        return float(nums[0]) * float(nums[1])

    def divide(self, nums):
        try:
            return float(nums[0]) / float(nums[1])
        except ZeroDivisionError:
            return "Error: division by zero!"

    def detect_action(self):
        if '+' in self.expr:
            nums = self.expr.split('+')
            self.show_on_display(self.add(nums))
        elif '-' in self.expr:
            nums = self.expr.split('-')
            self.show_on_display(self.subtract(nums))  
        elif '*' in self.expr:
            nums = self.expr.split('*')
            self.show_on_display(self.multiply(nums))
        elif '/' in self.expr:
            nums = self.expr.split('/')
            self.show_on_display(self.divide(nums))

    def show_on_display(self, num):
        self.display.set(num)

    def press(self, button):
        self.expr += str(button)
        self.display.set(self.expr)
    
    def clear_display(self):
        self.expr = ""
        self.display.set(self.expr)



# create a calculator
app = Calculator()
app.window.mainloop()