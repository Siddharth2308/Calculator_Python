from tkinter import*
from tkinter.messagebox import*
from PIL import Image
import math as m
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
font = ('arial', 18, 'bold ')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def all_clear():
    textField.delete(0, END)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def clear():
    ex = textField.get()
    ex = ex[0:len(ex) -1]
    textField.delete(0,END)
    textField.insert(0,ex)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def click_btn_function(event):
    print("btn clicked")
    b = event.widget
    text = b['text']
    print(text)
    if text == 'X':
        textField.insert(END,'*')
        return;
    if text == '÷':
        textField.insert(END,'/')

    if text =='=':
        try:
            ex = textField.get()
            answer = eval(ex)
            textField.delete(0,END)
            textField.insert(0,answer)
            return;
        except Exception as e:
            print("Error", e)
            showerror("Error", e)
    textField.insert(END,text)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
window = Tk()
window.title("E13menT's Calculator")
window.configure(background='powder blue')
window.geometry('350x550')
window.iconbitmap(r'calcu.ico')
#pic = PhotoImage(file='maths.png')
#headinglabel = Label(window,image = pic)
#new_size = pic.resize((15,15))
#headinglabel.pack(side=TOP,pady = 10)
heading =  Label(window, text="E13menT's Calculator", font = ('arial', 22, 'bold underline'), bg ='powder blue' )
heading.pack(side = TOP)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
textField = Entry(window, font = font,bd=30, insertwidth=4,bg="powder blue", justify= CENTER)
textField.pack(side = TOP, pady = 10, fill = X, padx = 10)
buttonFrame=Frame(window, bg ='powder blue')
buttonFrame.pack(side = TOP)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
temp = 1
for i in range (0,3):
    for j in range(0,3):
        btn = Button(buttonFrame, text = str(temp), font = font, padx=5,pady=3,bd=8,width = 3, fg="black",bg="powder blue", activebackground ='orange',activeforeground ='white')
        btn.grid(row = i, column = j,padx=2,pady=2)
        temp = temp + 1
        btn.bind('<Button-1>',click_btn_function)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
zeroBtn = Button(buttonFrame, text = '0', font = font, padx=5,pady=3,bd=8,width = 3, fg="black",bg="powder blue", activebackground ='orange',activeforeground ='white')
zeroBtn.grid(row = 3, column = 0,padx=2,pady=2)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
dotBtn = Button(buttonFrame, text = '.', font = font, padx=5,pady=3,bd=8,width = 3, fg="black",bg="powder blue", activebackground ='orange',activeforeground ='white')
dotBtn.grid(row = 3, column = 1,padx=2,pady=2)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
equalBtn = Button(buttonFrame, text = '=', font = font, padx=5,pady=3,bd=8,width = 3, fg="black",bg="powder blue", activebackground ='orange',activeforeground ='white')
equalBtn.grid(row = 3, column = 2,padx=2,pady=2)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
plusBtn = Button(buttonFrame, text = '+', font = font, padx=5,pady=3,bd=8,width = 3, fg="black",bg="powder blue", activebackground ='orange',activeforeground ='white')
plusBtn.grid(row = 0, column = 3,padx=2,pady=2)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
minusBtn = Button(buttonFrame, text = '−', font = font, padx=5,pady=3,bd=8,width = 3, fg="black",bg="powder blue", activebackground ='orange',activeforeground ='white')
minusBtn.grid(row = 1, column = 3,padx=2,pady=2)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
multBtn = Button(buttonFrame, text = 'X', font = font, padx=5,pady=3,bd=8,width = 3, fg="black",bg="powder blue", activebackground ='orange',activeforeground ='white')
multBtn.grid(row = 2, column = 3,padx=2,pady=2)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
divideBtn = Button(buttonFrame, text = '/', font = font, padx=5,pady=3,bd=8,width = 3, fg="black",bg="powder blue", activebackground ='orange',activeforeground ='white')
divideBtn.grid(row = 3, column = 3,padx=2,pady=2)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
clearBtn = Button(buttonFrame, text = '⌫', font = font, padx=5,pady=3,bd=8, width = 8,fg="black",bg="powder blue", activebackground ='orange',activeforeground ='white',command = clear)
clearBtn.grid(row = 4, column = 0,columnspan=2,padx=2,pady=2)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
clearBtn = Button(buttonFrame, text = 'AC', font = font, padx=5,pady=3,bd=8,width = 8, fg="black",bg="powder blue", activebackground ='orange',activeforeground ='white',command = all_clear)
clearBtn.grid(row = 4, column = 2,columnspan=2,padx=2,pady=2)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
zeroBtn.bind('<Button-1>',click_btn_function)
dotBtn.bind('<Button-1>',click_btn_function)
equalBtn.bind('<Button-1>',click_btn_function)
plusBtn.bind('<Button-1>',click_btn_function)
minusBtn.bind('<Button-1>',click_btn_function)
multBtn.bind('<Button-1>',click_btn_function)
divideBtn.bind('<Button-1>',click_btn_function)
def enterClick(event):
    e = Event()
    e.widget = equalBtn
    click_btn_function(e)
textField.bind('<Return>',enterClick)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Scientific Calculator & Programmer's Calculator
scFrame = Frame(window)
pcFrame = Frame(window)

sqrtBtn = Button(scFrame, text='√', font=('arial', 15,'bold'),bd=8, fg="black",bg="powder blue", width=5,activebackground='orange',
                 activeforeground='white')
sqrtBtn.grid(row=0, column=0)
powBtn = Button(scFrame, text='^', font=('arial', 15,'bold'),bd=8, fg="black",bg="powder blue", width=5,activebackground='orange',
                activeforeground='white')
powBtn.grid(row=0, column=1)
factBtn = Button(scFrame, text='x!', font=('arial', 15,'bold'),bd=8, fg="black",bg="powder blue", width=5, activebackground='orange',
                 activeforeground='white')
factBtn.grid(row=0, column=2)
radBtn = Button(scFrame, text='toRad', font=('arial', 15,'bold'),bd=8, fg="black",bg="powder blue", width=5,activebackground='orange',
                activeforeground='white')
radBtn.grid(row=0, column=3)
degBtn = Button(scFrame, text='toDeg', font=('arial', 15,'bold'),bd=8, fg="black",bg="powder blue", width=5,activebackground='orange',
                activeforeground='white')
degBtn.grid(row=1, column=0)
sinBtn = Button(scFrame, text='sinθ', font=('arial', 15,'bold'),bd=8, fg="black",bg="powder blue", width=5, activebackground='orange',
                activeforeground='white')
sinBtn.grid(row=1, column=1)
cosBtn = Button(scFrame, text='cosθ', font=('arial', 15,'bold'),bd=8, fg="black",bg="powder blue", width=5, activebackground='orange',
                activeforeground='white')
cosBtn.grid(row=1, column=2)
tanBtn = Button(scFrame, text='tanθ', font=('arial', 15,'bold'),bd=8, fg="black",bg="powder blue", width=5, activebackground='orange',
                activeforeground='white')
tanBtn.grid(row=1, column=3)
#------------------------------------------------------------------------------------------------------------------------------------------------
hexBtn = Button(pcFrame, text='hex', font=('arial', 15,'bold'),bd=8, fg="black",bg="powder blue", width=5, activebackground='orange',
                activeforeground='white')
hexBtn.grid(row=0, column=0)
binBtn = Button(pcFrame, text='bin', font=('arial', 15,'bold'),bd=8, fg="black",bg="powder blue", width=5, activebackground='orange',
                activeforeground='white')
binBtn.grid(row=0, column=1)
octBtn = Button(pcFrame, text='oct', font=('arial', 15,'bold'),bd=8, fg="black",bg="powder blue", width=5, activebackground='orange',
                activeforeground='white')
octBtn.grid(row=0, column=2)
intBtn = Button(pcFrame, text='int', font=('arial', 15,'bold'),bd=8, fg="black",bg="powder blue", width=5, activebackground='orange',
                activeforeground='white')
intBtn.grid(row=0, column=3)
logBtn = Button(pcFrame, text='log', font=('arial', 15,'bold'),bd=8, fg="black",bg="powder blue", width=5, activebackground='orange',
                activeforeground='white')
logBtn.grid(row=1, column=0)
avogodBtn = Button(pcFrame, text='NA', font=('arial', 15,'bold'),bd=8, fg="black",bg="powder blue", width=5, activebackground='orange',
                activeforeground='white')
avogodBtn.grid(row=1, column=1)
modBtn = Button(pcFrame, text='±', font=('arial', 15,'bold'),bd=8, fg="black",bg="powder blue", width=5, activebackground='orange',
                activeforeground='white')
modBtn.grid(row=1, column=2)
piBtn = Button(pcFrame, text='π', font=('arial', 15,'bold'),bd=8, fg="black",bg="powder blue", width=5, activebackground='orange',
                activeforeground='white')
piBtn.grid(row=1, column=3)
normalcalci = True
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def calculate_sc(event):
    print('btn...')
    btn = event.widget
    text =btn['text']
    print(text)
    ex = textField.get()
    answer = ''
    if text == 'toDeg':
        print("cal degree")
        answer = str(m.degrees(float(ex)))
    elif text == 'toRad':
        print('radian')
        answer = str(m.radians(float(ex)))
    elif text == 'x!':
        print("cal factorial")
        answer = str(m.factorial(int(ex)))
    elif text == 'sinθ':
        print("cal sin")
        answer = str(m.sin(m.radians(int(ex))))
    elif text == 'cosθ':
        answer = str(m.cos(m.radians(int(ex))))
    elif text == 'tanθ':
        answer = str(m.tan(m.radians(int(ex))))
    elif text == '√':
        print('sqrt')
        answer = m.sqrt(int(ex))
    elif text == '^':
        print('pow')
        base, pow = ex.split(',')
        print(base)
        print(pow)
        answer = m.pow(int(base), int(pow))
    textField.delete(0,END)
    textField.insert(0,answer)
def pc_calculate(event):
    print('btn...')
    btn = event.widget
    text =btn['text']
    print(text)
    ex = textField.get()
    answer = ''
    if text == 'hex':
        answer = str(hex(int(ex)))
    elif text == 'bin':
        answer = str(bin(int(ex)))
    elif text == 'oct':
        answer = str(oct(int(ex)))
    elif text =='int':
        answer = str(int(ex))
    elif text == 'log':
        answer = str(m.log(int(ex)))
    elif text == 'NA':
        answer = '6.0221409e+23'
    elif text == '±':
        answer = ('-',textField.get())
    elif text == 'π':
        answer = str(float(3.142857142857143))
    textField.delete(0,END)
    textField.insert(0,answer)

def sc_click():
    global normalcalci
    if normalcalci:
        buttonFrame.pack_forget()
        scFrame.pack(side=TOP, pady=10)
        buttonFrame.pack(side=TOP)
        window.geometry('350x650')
        print('Show Scientific view')
        normalcalci = False
    else:
        print('Show Normal View')
        scFrame.pack_forget()
        window.geometry('350x550')
        normalcalci = True
def pc_click():
    global normalcalci
    if normalcalci:
        buttonFrame.pack_forget()
        buttonFrame.pack(side=TOP, pady=10)
        pcFrame.pack(side=TOP)
        window.geometry('350x675')
        print('Show Programming View')
        normalcalci = False
    else:
        print('Show Normal View')
        pcFrame.pack_forget()
        window.geometry('350x550')
        normalcalci = True
def global_mode():
    global normalcalci
    if normalcalci:
        buttonFrame.pack_forget()
        scFrame.pack(side=TOP, pady=10)
        buttonFrame.pack(side=TOP,pady=10)
        pcFrame.pack(side=TOP)
        window.geometry('350x775')
        print('Show global View')
        normalcalci = False
    else:
        print('Show Normal View')
        pcFrame.pack_forget()
        scFrame.pack_forget()
        window.geometry('350x550')
        normalcalci = True
def guide_click():
    a = "You can use the keyboard of buttons provided for input. for using Scientific Mode select the correspondig mode in the menu. "
    print("This is a Guide")
    showerror("Guide", a)
def exit():
    print("Closing Window")
    window.destroy()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
sqrtBtn.bind("<Button-1>",calculate_sc)
radBtn.bind("<Button-1>",calculate_sc)
degBtn.bind("<Button-1>",calculate_sc)
powBtn.bind("<Button-1>",calculate_sc)
factBtn.bind("<Button-1>",calculate_sc)
sinBtn.bind("<Button-1>",calculate_sc)
cosBtn.bind("<Button-1>",calculate_sc)
tanBtn.bind("<Button-1>",calculate_sc)
hexBtn.bind("<Button-1>",pc_calculate)
binBtn.bind("<Button-1>",pc_calculate)
avogodBtn.bind("<Button-1>",pc_calculate)
modBtn.bind("<Button-1>",pc_calculate)
logBtn.bind("<Button-1>",pc_calculate)
octBtn.bind("<Button-1>",pc_calculate)
piBtn.bind("<Button-1>",pc_calculate)
intBtn.bind("<Button-1>",pc_calculate)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
fontMenu = ('', 15)
menuBar = Menu(window)
mode = Menu(menuBar, font=fontMenu, tearoff = 0)
mode.add_checkbutton(label="Scientific Calculator", command = sc_click)
mode.add_checkbutton(label="Programmer Calculator", command = pc_click)
mode.add_checkbutton(label="Global Mode", command = global_mode)
menuBar.add_cascade(label="Mode",menu=mode)
menuBar.add_command(label="Guide",command = guide_click)
menuBar.add_command(label="Exit",command = exit)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

window.config(menu=menuBar)
window.mainloop()
#Author- E13menT
