import random
import tkinter as tk

def showoutput():

    number = int(text_input.get())

    if number == 0:
        output_lebel.configure(text= 'คิดเองบ้างสิ ')
        return

    output = ''
    for i in range(1,19):
        output += str(number) + 'x' + str(i)
        output += " = " + str(number * i) + "\n"

    output_lebel.configure(text=output)

window = tk.Tk()
window.title("Hello world")
window.minsize(width=120,height=400)

title_label = tk.Label(master=window,text="สูตรคูณแม่ \n",)
title_label.pack(side=tk.TOP,fill= tk.BOTH)

text_input = tk.Entry(master=window ,width=5)
text_input.pack()

title_label = tk.Label(master=window,text="\n",height=1)
title_label.pack()

ok_button = tk.Button(
    master=window,text="ได้แก่",
    command=showoutput
)
ok_button.pack()

output_lebel = tk.Label(master=window)
output_lebel.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

#fist project
window.mainloop()
