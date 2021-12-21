from tkinter import *
import math
import parser
import tkinter.messagebox

function = Tk()
function.title("Engineering Scientific Calculator")
function.configure(background = "blue")
function.resizable(width=False, height= False)
function.geometry("480x568+0+0")

calc = Frame(function)
calc.grid()

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def EnterNum(self,num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if  self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())    

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == 'add':
            self.total+=self.current
        if self.op == 'sub':
            self.total-=self.current
        if self.op == 'multi':
            self.total*=self.current 
        if self.op == 'divide':
            self.total/=self.current   
        if self.op == 'mod':        
            self.total%=self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True            
        self.op = op
        self.result = False

    def clear_entry(self):
        self.result = False
        self.current = '0'
        self.display(0)
        self.input_value = True

    def all_clear_entry(self):
        self.clear_entry()
        self.total = 0    

    def mathsPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squareRoot(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)
    
    def Cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def Sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def Cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def Sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def arcCos(self):
        self.result = False
        self.current = math.acos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def arcSin(self):
        self.result = False
        self.current = math.asin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def arctan(self):
        self.result = False
        self.current = math.atan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def Deg(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)    

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)
   
    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)
    
    def Exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)
    
    def lGamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    def Pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)
    
    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)    
    

added_value = Calc()
txtDisplay = Entry(calc, font=('arial',20,'bold'), bg='yellow', bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, '0')

numberpad = '789456123'
i = 0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width= 6, height=2, font=('arial',20,'bold'), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]['command'] = lambda x = numberpad[i]: added_value.EnterNum(x)
        i+=1
#===================================================#Business%Commercial Calculator=========================================================

btnClear = Button(calc, text=chr(67), width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command=added_value.clear_entry).grid(row=1,column=0,pady=1)

btnAllClear = Button(calc, text=chr(67) + chr(69), width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command=added_value.all_clear_entry).grid(row=1,column=1,pady=1)

btnsq = Button(calc, text='√', width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command= added_value.squareRoot).grid(row=1,column=2,pady=1)

btnAdd = Button(calc, text='+', width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command= lambda: added_value.operation('add')).grid(row=1,column=3,pady=1)

btnSub = Button(calc, text='-', width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command= lambda: added_value.operation('sub')).grid(row=2,column=3,pady=1)

btnMult = Button(calc, text='*', width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command= lambda: added_value.operation('multi')).grid(row=3,column=3,pady=1)

btnDiv = Button(calc, text=chr(247), width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command= lambda: added_value.operation('divide')).grid(row=4,column=3,pady=1)

btnZero = Button(calc, text='0', width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command= lambda: added_value.EnterNum(0)).grid(row=5,column=0,pady=1)

btnDot = Button(calc, text='.', width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command= lambda: added_value.EnterNum('.')).grid(row=5,column=1,pady=1)

btnPM = Button(calc, text=chr(177), width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command=added_value.mathsPM).grid(row=5,column=2,pady=1)

btnEquals = Button(calc, text='=', width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command=added_value.sum_of_total).grid(row=5,column=3,pady=1)

#===================================================#Engineering&Scientific Calculator=====================================================

btnPi = Button(calc, text='π', width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command= added_value.Pi).grid(row=1,column=4,pady=1)

btnCos = Button(calc, text='cos', width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command= added_value.Cos).grid(row=1,column=5,pady=1)

btntan = Button(calc, text='tan', width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command= added_value.tan).grid(row=1,column=6,pady=1)

btnsin = Button(calc, text='sin', width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command= added_value.Sin).grid(row=1,column=7,pady=1)

#=================================================================================================================================

btn2Pi = Button(calc, text='2π', width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command= added_value.tau).grid(row=2,column=4,pady=1)

btnCosh = Button(calc, text='cosh', width=6, height=2, font=('arial',20,'bold'), bd=4, 
command= added_value.Cosh).grid(row=2,column=5,pady=1)

btnSinh = Button(calc, text='sinh', width=6, height=2, font=('arial',20,'bold'), bd=4, 
command= added_value.Sinh).grid(row=2,column=6,pady=1)

btndeg = Button(calc, text='deg', width=6, height=2, font=('arial',20,'bold'), bd=4, 
command=added_value.Deg).grid(row=2,column=7,pady=1)

#=================================================================================================================================

btnlog = Button(calc, text='log', width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command= added_value.log).grid(row=3,column=4,pady=1)

btnExp = Button(calc, text='Exp', width=6, height=2, font=('arial',20,'bold'), bd=4, 
command= added_value.Exp).grid(row=3,column=5,pady=1)

btnMod = Button(calc, text='Mod', width=6, height=2, font=('arial',20,'bold'), bd=4, 
command= lambda: added_value.operation('mod')).grid(row=3,column=6,pady=1)

btnE = Button(calc, text='e', width=6, height=2, font=('arial',20,'bold'), bd=4, 
command=added_value.e).grid(row=3,column=7,pady=1)

#=================================================================================================================================

btnlog2 = Button(calc, text='log2', width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command= added_value.log2).grid(row=4,column=4,pady=1)

btnarctan = Button(calc, text='tan-1', width=6, height=2, font=('arial',20,'bold'), bd=4, 
command= added_value.arctan).grid(row=4,column=5,pady=1)

btnarcCos = Button(calc, text='cos-1', width=6, height=2, font=('arial',20,'bold'), bd=4, 
command= added_value.arcCos).grid(row=4,column=6,pady=1)

btnarcSin = Button(calc, text='sin-1', width=6, height=2, font=('arial',20,'bold'), bd=4, 
command= added_value.arcSin).grid(row=4,column=7,pady=1)

#=================================================================================================================================

btnlog10 = Button(calc, text='log10', width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command= added_value.log10).grid(row=5,column=4,pady=1)

btnlog1p = Button(calc, text='log1p', width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command= added_value.log1p).grid(row=5,column=5,pady=1)

btnexpm1 = Button(calc, text='expm1', width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command= added_value.expm1).grid(row=5,column=6,pady=1)

btnlgamma = Button(calc, text='lgamma', width=6, height=2, font=('arial',20,'bold'), bd=4, bg="blue", 
command= added_value.lGamma).grid(row=5,column=7,pady=1)

lblDisplay = Label(calc, text='Engineering Scientific Calculator', font=('arial',20,'bold'), justify=CENTER)
lblDisplay.grid(row=0, column=4, columnspan=4)

#===================================================Menu and Functions============================================================

def iExit():
    iExit = tkinter.messagebox.askyesno("Engineering Scientific Calculator", "Confirm if you want to exit")
    if iExit > 0:
        function.destroy()
        return

def Business_Commercial():
    function.resizable(width=False, height= False)
    function.geometry("480x568+0+0")

def Engineering_Scientific():
    function.resizable(width=False, height= False)
    function.geometry("944x568+0+0")


menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Business Commercial", command= Business_Commercial)
filemenu.add_command(label="Engineering Scientific", command= Engineering_Scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command= iExit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edits", menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="View Help")


function.config(menu = menubar)
function.mainloop()
