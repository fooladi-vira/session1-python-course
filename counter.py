import tkinter as tk
from tkinter import messagebox
def destroy_windows():
   # messagebox.showinfo('خروج','با موفقیت خارج شدید')
    if messagebox.askyesno('خروج','آیا میخواهید از برنامه خارج شوید؟'):
        root.destroy()
    
count = 0
def increase():
    global count
    count=count+1
    label.config(text=str(count))
    
def decrease():
    global count
    count=count-1
    label.config(text=str(count))  

# تعریف یک پنجره
root = tk.Tk(className='vira')
root.title('به کلاس پایتون خوش آمدید')
root.geometry('400x400+100+200')
root.resizable(width=False,height=False)
root.configure(bg='gold')

label = tk.Label(root, text="خوش آمدید!",bg="gray",font=14,fg="red")
# قرار دادن برچسب در پنجره
label.pack(side='top',fill='both')

btn_exit=tk.Button(root,text="خروج",font=14,fg="red",bg="black",command=destroy_windows)
btn_exit.pack(side='bottom',fill='both')

# تعریف یک برچسب برای نمایش مقدار شمارنده
label = tk.Label(root, text=str(count),font=50)

# تعریف یک دکمه برای افزایش شمارنده
button_up = tk.Button(root,text='+',font=50,border=5,bg="red",command=increase)

# تعریف یک دکمه برای کاهش شمارنده
button_down = tk.Button(root, text="-",font=50,border=5,bg="blue", command=decrease)

# قرار دادن عناصر در پنجره
label.pack(side='top',fill='both')
button_up.pack(side='top',fill='both')
button_down.pack(side='top',fill='both')
pic=tk.PhotoImage(file="1.png")
lable_pic=tk.Label(root,image=pic)
lable_pic.image=pic
lable_pic.pack(side='bottom',fill='both')
# نمایش پنجره
root.mainloop()
