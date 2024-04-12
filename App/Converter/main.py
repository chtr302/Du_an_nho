from tkinter import *

window = Tk()
window.title("Mile to KM Converter by Hau")
window.minsize(width=400,height=200)
window.config(padx=20,pady=20)

miles_input = Entry()
miles_input.grid(row = 0, column = 1)

miles_label = Label(text="Miles")
miles_label.grid(row=0,column=2)

is_equal_lebal = Label(text="is equal label")
is_equal_lebal.grid(row=1,column=0)

converts = Label(text="0")
converts.grid(row=1,column=1)

km = Label(text="Km")
km.grid(row=1,column=2)

def convert():
    miles = miles_input.get()
    km = float(miles) * 1.609
    converts.config(text=km)

caculate_button = Button(text="Calculate", command=convert)
caculate_button.grid(row=2,column=1)



window.mainloop()