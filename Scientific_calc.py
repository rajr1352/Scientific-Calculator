from tkinter import *
import math

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)


    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.show()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def show(self):
        if self.op == "add":
            self.total = self.total +  self.current
        if self.op == "minus":
            self.total = self.total - self.current
        if self.op == "mult":
            self.total = self.total * self.current
        if self.op == "divide":
            self.total = self.total / self.current
        if self.op == "raise":
            self.total = self.total ** self.current
        if self.op == "rootof":
            self.total = math.sqrt(self.total)
        if self.op == "fact":
            self.total=int(text_box.get())
            self.total=math.factorial(self.total)
        if self.op == "exp":
            self.total = math.exp(self.total)
        if self.op == "inv":
            self.total = 1/self.total
        if self.op == "sine":
            self.total = math.sin(self.total)
        if self.op == "cosine":
            self.total = math.cos(self.total)
        if self.op == "tangent":
            self.total=math.tan(self.total)
        if self.op == "ln":
            self.total=math.log(self.total)
        if self.op == "log":
            self.total=math.log(self.total,10)

        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.op_pending:
            self.show()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def clear(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_clear(self):
        self.clear()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)

sum1 = Calc()
root = Tk()
calc = Frame(root)
calc.grid()

root.title("Scientific_Calculator")
text_box = Entry(calc, justify=RIGHT,width=30,font=15)
text_box.grid(row = 0, column = 0,columnspan = 8,padx=30, pady = 30)
text_box.insert(0, "0")
#text_box.focus()

numbers = "789456123"
i = 0
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(Button(calc,height =2,width=4,padx=10, pady = 10, text = numbers[i]))
        bttn[i].grid(row = j, column = k,padx=1,pady=1)
        bttn[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
        i += 1

bttn_0 = Button(calc,height =2,width=4,padx=10, pady = 10, text = "0")
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row = 4, column = 0,  padx=1, pady = 1)

div = Button(calc,height =2,width=4,padx=10, pady = 10, text = "/")
div["command"] = lambda: sum1.operation("divide")
div.grid(row = 1, column = 3, padx=1, pady = 1)

mult = Button(calc,height =2,width=4,padx=10, pady = 10, text = "*")
mult["command"] = lambda: sum1.operation("mult")
mult.grid(row = 2, column = 3,  padx=1, pady = 1)

minus = Button(calc,height =2,width=4,padx=10, pady = 10, text = "-")
minus["command"] = lambda: sum1.operation("minus")
minus.grid(row = 3, column = 3, padx=1, pady = 1)

add = Button(calc,height =2,width=4,padx=10, pady = 10, text = "+")
add["command"] = lambda: sum1.operation("add")
add.grid(row = 4, column = 3,  padx=1, pady = 1)

power = Button(calc, height=2,width=4,padx=10,pady=10,text="x^y")
power["command"] = lambda: sum1.operation("raise")
power.grid(row=2,column = 4,padx=1,pady=1)

rootof = Button(calc, height=2, width=4, padx=10, pady=10, text="\/x")
rootof["command"] = lambda: sum1.operation("rootof")
rootof.grid(row=2, column=5, padx=1, pady=1)

exponent = Button(calc, height=2, width=4, padx=10, pady=10, text='e^x')
exponent["command"]=lambda: sum1.operation("exp")
exponent.grid(row=3,column=4,padx=1,pady=1)

inv = Button(calc, height=2, width=4, padx=10, pady=10, text="1/x")
inv["command"] = lambda: sum1.operation("inv")
inv.grid(row=4,column=4,padx=1,pady=1)

point = Button(calc,height =2,width=4,padx=10, pady = 10, text = ".")
point["command"] = lambda: sum1.num_press(".")
point.grid(row = 4, column = 1, padx=1, pady = 1)

sine = Button(calc, height=2, width=4, padx=10, pady=10, text="sin")
sine["command"] = lambda: sum1.operation("sine")
sine.grid(row=5, column=0, padx=1, pady=1)

cosine = Button(calc, height=2, width=4, padx=10, pady=10, text="cos")
cosine["command"] = lambda: sum1.operation("cosine")
cosine.grid(row=5, column=1, padx=1, pady=1)

tangent = Button(calc, height=2, width=4, padx=10, pady=10, text="tan")
tangent["command"] = lambda: sum1.operation("tangent")
tangent.grid(row=5, column=2, padx=1, pady=1)

loge = Button(calc, height=2, width=4, padx=10, pady=10, text="ln")
loge["command"] = lambda: sum1.operation("ln")
loge.grid(row=5, column=3, padx=1, pady=1)

log10 = Button(calc, height=2, width=4, padx=10, pady=10, text="log")
log10["command"] = lambda: sum1.operation("log")
log10.grid(row=5, column=4, padx=1, pady=1)

fact = Button(calc, height=2, width=4, padx=10, pady=10, text="fact")
fact["command"] = lambda: sum1.operation("fact")
fact.grid(row=3, column=5, padx=1, pady=1)


neg= Button(calc,height =2,width=4,padx=10, pady = 10, text = "+/-")
neg["command"] = sum1.sign
neg.grid(row = 4, column = 2,  padx=1, pady = 1)

clear = Button(calc,height =2,width=4,padx=10, pady = 10, text = "C")
clear["command"] = sum1.clear
clear.grid(row = 1, column = 4,  padx=1, pady = 1)

all_clear = Button(calc,height =2,width=4,padx=10, pady = 10, text = "AC")
all_clear["command"] = sum1.all_clear
all_clear.grid(row = 1, column = 5, padx=1, pady = 1)

equals = Button(calc,height =6,width=4,padx=10, pady = 10, text = "=")
equals["command"] = sum1.calc_total
equals.grid(row = 4, column = 5,columnspan=1,rowspan=2,padx=1, pady = 1)


root.mainloop()