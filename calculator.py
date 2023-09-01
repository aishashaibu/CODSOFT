import tkinter

base = tkinter.Tk()
base.title("Aisha's Calculator")

illustration = ""

def add(value):
    global illustration
    illustration += value
    label_sum.config(text=illustration)

def clear():
     global illustration
     illustration = ""
     label_sum.config(text=illustration)

def calculate():
    global illustration
    sum = ""
    if illustration != "":
        try:
            sum = eval(illustration)
        except:
            sum = "error" 
            illusrtation = ""   
    label_sum.config(text=sum)
    
label_sum =tkinter.Label(base,text="")
label_sum.grid(row=0,column=0, columnspan=4)

button_one = tkinter.Button(base, text="1",  height=4, width=9, bg ="maroon" , fg ="white", command=lambda: add("1"))
button_one.grid(row=1, column=0)

button_two = tkinter.Button(base, text="2", height=4, width=9,   bg ="maroon", fg ="white",  command=lambda: add("2"))
button_two.grid(row=1, column=1)

button_three= tkinter.Button(base, text="3",height=4, width=9,   bg ="maroon", fg ="white", command=lambda: add("3"))
button_three.grid(row=1, column=2)

button_multiplication= tkinter.Button(base, text="*",height=4, width=9,  bg ="maroon", fg ="white", command=lambda:add("*"))
button_multiplication.grid(row=1, column=3)

button_four = tkinter.Button(base, text="4",height=4, width=9,  bg ="maroon", fg ="white", command=lambda: add("4"))
button_four.grid(row=2, column=0)

button_five = tkinter.Button(base, text="5",height=4, width=9,  bg ="maroon", fg ="white", command=lambda: add("5"))
button_five.grid(row=2, column=1)

button_six = tkinter.Button(base, text="6",height=4, width=9, bg ="maroon", fg ="white", command=lambda: add("6"))
button_six.grid(row=2, column=2)

button_division= tkinter.Button(base, text="/",height=4, width=9,  bg ="maroon", fg ="white", command=lambda: add("/"))
button_division.grid(row=2, column=3)

button_seven= tkinter.Button(base, text="7",height=4, width=9, bg ="maroon", fg ="white", command=lambda: add("7"))
button_seven.grid(row=3, column=0)

button_eight = tkinter.Button(base, text="8",height=4, width=9, bg ="maroon", fg ="white", command=lambda: add("8"))
button_eight.grid(row=3, column=1)

button_nine = tkinter.Button(base, text="9",height=4, width=9, bg ="maroon", fg ="white", command=lambda: add("9"))
button_nine.grid(row=3, column=2)

button_addition= tkinter.Button(base, text="+",height=4, width=9, bg ="maroon", fg ="white", command=lambda: add("+"))
button_addition.grid(row=3, column=3)

button_clear= tkinter.Button(base, text="C",height=4, width=9, bg ="maroon", fg ="white", command=lambda: clear())
button_clear.grid(row=4, column=0)

button_zero= tkinter.Button(base, text="0",height=4, width=9,  bg ="maroon", fg ="white", command=lambda: add("0"))
button_zero.grid(row=4, column=1)

button_dot= tkinter.Button(base, text=".",height=4, width=9, bg ="maroon", fg ="white", command=lambda: add("."))
button_dot.grid(row=4, column=2)

button_subtraction= tkinter.Button(base, text="-",height=4, width=9, bg ="maroon", fg ="white", command=lambda: add("-"))
button_subtraction.grid(row=4, column=3)

button_equals= tkinter.Button(base, text="=",height=4, width=9,bg ="maroon", fg ="white", command=lambda: calculate())
button_equals.grid(row=5, column=0, columnspan=4)

base.mainloop()