from tkinter import *
import math 

root = Tk()
blank_space= " "
root.title(50 * blank_space + "VS code Calculation")
root.resizable(width = FALSE, height=False)
root.geometry("438x573+460+40")

coverFrame = Frame (root, bd=20, pady=2, relief = RIDGE)
coverFrame.grid()

coverMainFrame = Frame (coverFrame, bd=10, pady=2,bg='purple', relief = RIDGE)
coverMainFrame.grid()

MainFrame = Frame (coverMainFrame, bd=5, pady=2, relief = RIDGE)
MainFrame.grid()

class calculator():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value= True
        self.check_sum = False
        self.op = ""
        self.result = False
    def numberEnter(self,num):
        self.result = False
        firstnum = entDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum 
            self.input_value= False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def display(self,value):
        entDisplay.delete(0,END)
        entDisplay.insert(0,value)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(entDisplay.get())

        if self.total.is_integer():
            self.total = int(self.total)
        self.display(self.total)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "mult":
            self.total *= self.current
        if self.op == "div":
            self.total /= self.current
        if self.op == "floor":
            self.total //= self.current
        if self.op == "modulus":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)
    
    def operation(self,op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.results = False

    def backspace(self):
        numlen = len(entDisplay.get())
        entDisplay.delete(numlen - 1, 'end')
        if numlen == 1:
            entDisplay.insert(0,"0")

    def clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True
            

added_value = calculator()
entDisplay = Entry(MainFrame, font=('arial',19,'bold'), bd=14, width=26,bg='#BE93D4', justify=RIGHT)
entDisplay.grid(row=0,column=0,columnspan=4, pady=1)
entDisplay.insert(0,"0")

numpad = "789456123"
i = 0
btn =[]

for j in range(3,6):
    for k in range(3):
        btn.append(Button(MainFrame,width=6, height=2,font=('arial',17,'bold'), bd=4, text=numpad[i]))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]["command"]=lambda x=numpad[i]: added_value.numberEnter(x)
        i += 1
btnBackSpace=Button(MainFrame,width=6, height=2,font=('arial',17,'bold'), bd=4, text="🔙",bg='violet', command= added_value.backspace)
btnBackSpace.grid(row=1, column=0, pady=1)

btnClear=Button(MainFrame,width=6, height=2,font=('arial',17,'bold'), bd=4, text=chr(67),bg='violet',command= added_value.clear_Entry)
btnClear.grid(row=1, column=1, pady=1)

btnFloor=Button(MainFrame,width=6, height=2,font=('arial',17,'bold'), bd=4, text="//",bg='violet',command=lambda:added_value.operation("floor"))
btnFloor.grid(row=1, column=2, pady=1)

btnModulus=Button(MainFrame,width=6, height=2,font=('arial',17,'bold'), bd=4, text="%",bg='violet',command=lambda:added_value.operation("modulus"))
btnModulus.grid(row=1, column=3, pady=1)

btnAdd=Button(MainFrame,width=6, height=2,font=('arial',17,'bold'), bd=4, text="+",bg='violet', command=lambda:added_value.operation("add"))
btnAdd.grid(row=3, column=3, pady=1)

btnSub=Button(MainFrame,width=6, height=2,font=('arial',17,'bold'), bd=4, text="-",bg='violet',command=lambda:added_value.operation("sub"))
btnSub.grid(row=4, column=3, pady=1)

btnMult=Button(MainFrame,width=6, height=2,font=('arial',17,'bold'), bd=4, text="*",bg='violet',command=lambda:added_value.operation("mult"))
btnMult.grid(row=5, column=3, pady=1)

btnDiv=Button(MainFrame,width=6, height=2,font=('arial',17,'bold'), bd=4, text=chr(247),bg='violet',command=lambda:added_value.operation("div"))
btnDiv.grid(row=6, column=3, pady=1)

btnZero=Button(MainFrame,width=6, height=2,font=('arial',17,'bold'), bd=4, text="0",command=lambda:added_value.numberEnter("0"))
btnZero.grid(row=6, column=0, pady=1)

btndot=Button(MainFrame,width=6, height=2,font=('arial',17,'bold'), bd=4, text=".",bg='violet',command=lambda:added_value.numberEnter("."))
btndot.grid(row=6, column=1, pady=1)

btnEquals=Button(MainFrame,width=6, height=2,font=('arial',17,'bold'), bd=4, text="=",bg='violet', command = added_value.sum_of_total)
btnEquals.grid(row=6, column=2, pady=1)

root.mainloop()
