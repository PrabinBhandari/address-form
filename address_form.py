import tkinter as tk

window = tk.Tk()
window.title("Address Entry Form")

frame = tk.Frame(master= window, relief = tk.SUNKEN, borderwidth =3)
frame.pack()

label1 = tk.Label(text = "First Name: ", master = frame )
entry1 = tk.Entry(master= frame, width=50)
label1.grid(row=0, column=0, sticky="e")
entry1.grid(row=0, column=1)

label2 = tk.Label(text = "Last Name: ", master = frame)
entry2 = tk.Entry(master= frame, width=50)
label2.grid(row=1, column=0, sticky="e")
entry2.grid(row=1, column=1)

label3 = tk.Label(text = "Address Line 1: ", master = frame )
entry3 = tk.Entry(master= frame, width=50)
label3.grid(row=2, column=0, sticky=tk.E)
entry3.grid(row=2, column=1)

label4 = tk.Label(text = "Address Line 2: ", master = frame )
entry4 = tk.Entry(master= frame, width=50)
label4.grid(row=3, column=0, sticky=tk.E)
entry4.grid(row=3, column=1)

label5 = tk.Label(text = "City: ", master = frame )
entry5 = tk.Entry(master= frame, width=50)
label5.grid(row=5, column=0, sticky=tk.E)
entry5.grid(row=5, column=1)

label6 = tk.Label(text = "State/Province: ", master = frame )
entry6 = tk.Entry(master= frame, width=50)
label6.grid(row=6, column=0, sticky=tk.E)
entry6.grid(row=6, column=1)

label7 = tk.Label(text = "Postal Code: ", master = frame )
entry7 = tk.Entry(master= frame, width=50)
label7.grid(row=7, column=0, sticky=tk.E)
entry7.grid(row=7, column=1)

label8 = tk.Label(text = "Country: ", master = frame )
entry8 = tk.Entry(master= frame, width=50)
label8.grid(row=8, column=0, sticky=tk.E)
entry8.grid(row=8, column=1)

buttons =tk.Frame()
buttons.pack(fill=tk.X,ipadx=5, ipady=5)

def submit_click():
    file = open("py.txt",'a')
    file.write("\n")
    file.write(entry1.get()+"\n")
    file.write(entry2.get()+"\n")
    file.write(entry3.get()+"\n")
    file.write(entry4.get()+"\n")
    file.write(entry5.get()+"\n")
    file.write(entry6.get()+"\n")
    file.write(entry7.get()+"\n")
    file.write(entry8.get()+"\n")
    file.close()

def drop():
    entry1.delete(first=0, last=tk.END)
    entry2.delete(first=0, last=tk.END)
    entry3.delete(first=0, last=tk.END)
    entry4.delete(first=0, last=tk.END)
    entry5.delete(first=0, last=tk.END)
    entry6.delete(first=0, last=tk.END)
    entry7.delete(first=0, last=tk.END)
    entry8.delete(first=0, last=tk.END)
  

button_submit = tk.Button(master= buttons,text= "Submit", command = submit_click)
button_submit.pack(side = tk.RIGHT, padx = 10, ipadx=10)

button_clear = tk.Button(master= buttons,text="Clear", command = drop)
button_clear.pack(side = tk.RIGHT, ipadx = 10)

window.mainloop()