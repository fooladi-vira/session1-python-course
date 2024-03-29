import tkinter as tk
import random

def set_user_choice(choice):
    global user_choice
    user_choice = choice





# تعریف یک پنجره
root = tk.Tk()

# تعریف متغیرهای برای ذخیره انتخاب کاربر و کامپیوتر
user_choice = ""
computer_choice = ""

# تعریف یک برچسب برای نمایش پیام
label = tk.Label(root, text="")

# تعریف یک دکمه برای انتخاب سنگ
button_rock = tk.Button(root, text="سنگ",command=set_user_choice("سنگ"))

# تعریف یک دکمه برای انتخاب کاغذ
button_paper = tk.Button(root, text="کاغذ", command=set_user_choice("کاغذ"))

# تعریف یک دکمه برای انتخاب قیچی
button_scissors = tk.Button(root, text="قیچی", command=set_user_choice("قیچی"))

# قرار دادن عناصر در پنجره
label.pack()
button_rock.pack()
button_paper.pack()
button_scissors.pack()

# تابع برای تعیین برنده بازی
def determine_winner():
    global user_choice, computer_choice

    # تعیین برنده بر اساس انتخاب کاربر و کامپیوتر
    if user_choice == computer_choice:
        return "مساوی"
    elif (user_choice == "سنگ" and computer_choice == "کاغذ") or (user_choice == "کاغذ" and computer_choice == "قیچی") or (user_choice == "قیچی" and computer_choice == "سنگ"):
        return "کامپیوتر"
    else:
        return "کاربر"

# تابع برای نمایش پیام برنده بازی
def show_winner():
    global label

    # تعیین برنده بازی
    winner = determine_winner()

    # نمایش پیام برنده بازی
    label.config(text=winner)

# تعریف یک حلقه برای اجرای بازی
while True:
    # انتخاب تصادفی انتخاب کامپیوتر
    computer_choice = ["سنگ", "کاغذ", "قیچی"][random.randint(0, 2)]

    # تعیین برنده بازی
    winner = determine_winner()

    # نمایش پیام برنده بازی
    show_winner()

    # بررسی اینکه کاربر می‌خواهد بازی را ادامه دهد یا خیر
    if input("آیا می‌خواهید بازی را ادامه دهید (Y/N)؟ ") != "Y":
        break

# نمایش پیام پایان بازی
label.config(text="پایان بازی")

# نمایش پنجره
root.mainloop()
