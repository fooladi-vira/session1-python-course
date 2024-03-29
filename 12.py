import tkinter as tk
from tkinter import messagebox
def show():
    name=box_name.get()
    if name=='mamad':
        tk.messagebox.askyesno('نمایش پیام','اصلا بهم گوش نمیدی '+name)
    else:
        tk.messagebox.showinfo('نمایش پیام','سلام '+name)
# تعریف یک پنجره
root=tk.Tk()
root.geometry('700x800+200+100')
root.resizable(width=False,height=False)
root.configure(bg='Aqua')
root.title('نمایش پیام')
#برچسب
lable_name=tk.Label(root,text='نام خود را وارد کنید',font=('B Nazanin',25),fg="blue")
lable_name.pack()

box_name=tk.Entry(root,font=('B Nazanin',25),fg="red")
box_name.pack()

btn_show=tk.Button(root,text='نمایش پیام',font=('B Nazanin',25),fg="blue",command=show)
btn_show.pack()
root.mainloop()


