import tkinter as tk
count=0
def increase():
    global count
    count=count+1
    label.config(text=str(count))
def decrease():
    global count
    count=count-1
    label.config(text=str(count))  
root = tk.Tk(className='vira')
root.title('به کلاس پایتون خوش آمدید')
root.geometry('400x400+100+200')
root.resizable(width=False,height=False)
root.configure(bg='gold')
label = tk.Label(root, text="شمارنده",bg="gray",font=14,fg="black")
label.pack(side='top',fill='both')
label = tk.Label(root, text=str(count),font=50)
label.pack(side='top',fill='both')
button_up = tk.Button(root,text='+',font=50,border=5,bg="red",command=increase)
button_up.pack(side='top',fill='both')
button_down = tk.Button(root, text="-",font=50,border=5,bg="blue", command=decrease)
button_down.pack(side='top',fill='both')
root.mainloop()