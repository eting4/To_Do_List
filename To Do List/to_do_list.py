from tkinter import *

def add_with_return_key(event): 
    listbox.insert(listbox.size(),entry.get())
    entry.delete(0,'end')
    
def add(): 
    listbox.insert(listbox.size(),entry.get())
    entry.delete(0,'end')

def delete(): 
    for index in reversed(listbox.curselection()): 
        listbox.delete(index)

window = Tk()
window.geometry('400x350')
window.title('Sticky Note')
window.bind('<Return>', add_with_return_key)

icon = PhotoImage(file='stickynote3.png')
window.iconphoto(True,icon)

listbox = Listbox(window,
                  bg='#f7ffde',
                  fg='black',
                  selectmode=MULTIPLE,
                  )
listbox.pack(fill=BOTH,expand=True)

buttons = Frame(window,bg='brown')
buttons.pack()
addButton = Button(buttons,text='add task',command=add)
addButton.config(borderwidth=0,highlightthickness=0)
addButton.pack(side=LEFT)
deleteButton = Button(buttons,text='delete task',command=delete)
deleteButton.config(borderwidth=0,highlightthickness=0)
deleteButton.pack(side=LEFT)

entry = Entry(window,bg='black',relief=FLAT)
entry.pack()

window.mainloop()