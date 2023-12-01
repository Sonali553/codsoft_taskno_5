from tkinter import *
root = Tk()
root.geometry('520x280')
root.config(bg = 'slateGray3')
root.resizable(0, 0)
root.title('contack book')
contactlist = []
Name = StringVar()
Number = StringVar()

frame = Frame(root)
frame.pack(side = RIGHT)
scroll = Scrollbar(frame, orient = VERTICAL)
select = Listbox(frame, yscrollcommand = scroll.set, height = 12)
scroll.config(command = select.yview)
scroll.pack(side = RIGHT, fill = Y)
select.pack(side = LEFT, fill = BOTH, expand = 1)

def Selected():
    return int(select.curselection()[0])

def AddContact():
    contactlist.append([Name.get(), Number.get()])
    Select_set()

def EDIT():
    contactlist[Selected()] = [Name.get(), Number.get()]
    Select_set()

def DELETE():
    del contactlist[Selected()]
    Select_set()

def VIEW():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)

def EXIT():
    root.destroy()

def RESET():
    Name.set('')
    Number.set('')

def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)
Select_set()

Label(root, text = 'NAME', font = 'arial 12 bold', bg = 'SlateGray3').place(x = 30, y = 20)
Entry(root, textvariable = Name).place(x = 100, y = 20)

Label(root, text = 'PHONE NO', font = 'arial 12 bold', bg = 'SlateGray3').place(x = 30, y = 70)
Entry(root, textvariable = Number).place(x = 130,  y = 70)

Button(root, text = "ADD", font = 'arial 12 bold', bg = 'SlateGray4', command = AddContact).place(x =  50, y = 110)

Button(root, text = "EDIT", font = 'arial 12 bold', bg = 'SlateGray4', command = EDIT).place(x =  160, y = 110)

Button(root, text = "DELETE", font = 'arial 12 bold', bg = 'SlateGray4', command = DELETE).place(x =  50, y = 170)

Button(root, text = "VIEW", font = 'arial 12 bold', bg = 'SlateGray4', command = VIEW).place(x =  160, y = 170)

Button(root, text = "EXIT", font = 'arial 12 bold', bg = 'red', command = EXIT).place(x =  250, y = 110)

Button(root, text = "RESET", font = 'arial 12 bold', bg = 'SlateGray4', command = RESET).place(x =  250, y = 170)
root.mainloop()
