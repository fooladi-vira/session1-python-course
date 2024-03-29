import tkinter as tk
from tkinter import PhotoImage

def destroy_windows():
    root.destroy()
    
def show_pic():
    pic=PhotoImage(file="1.png")
    lable_pic=tk.Label(root,image=pic)
    lable_pic.image=pic
    lable_pic.pack(side='bottom',fill='both')

# تعریف یک پنجره
root = tk.Tk()
root.geometry('700x600+600+100')
root.configure(bg='Aqua')
root.resizable(width=False,height=False)
# تعریف یک برچسب
label = tk.Label(root, text="خوش آمدید!",bg="gray",font=14,fg="red")
# قرار دادن برچسب در پنجره
label.pack(side='top',fill='both')

btn_exit=tk.Button(root,text="خروج",font=14,fg="red",bg="black",command=destroy_windows)
btn_exit.pack(side='bottom',fill='both')
btn_pic=tk.Button(root,text="نمایش عکس",font=14,fg="red",bg="yellow",command=show_pic)
btn_pic.pack(side='top',fill='both')

# نمایش پنجره
root.mainloop()


