import tkinter as tk
# تعریف یک پنجره
root = tk.Tk()
root.geometry('700x600+600+100')
root.resizable(width=False,height=False)
root.configure(bg='Aqua')
root.title('نرم افزار آموزشگاه ویرا')


lbl_2=tk.Label(root,text=" آموزشگاه ویرا",font=35,fg="blue")
lbl_2.pack(side='bottom',fill='both')

lbl_3=tk.Label(root,text=" آموزشگاه ویرا",font=45,fg="gold")
lbl_3.pack(side='bottom',fill='both')

lbl_4=tk.Label(root,text=" آموزشگاه ویرا",font=55,fg="black")
lbl_4.pack(side='top',fill='both')

lbl_1=tk.Label(root,text=" آموزشگاه ویرا",font=25,fg="red")
lbl_1.pack(side='bottom',fill='both')
# نمایش پنجره
root.mainloop()
