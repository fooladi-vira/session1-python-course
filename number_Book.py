# name and number
number_dict={'ali':'09173701234',
             'zahra':'09107101234',
             'mohamad':'09111201234',
             'roz':'09131201234'}
# گرفتن اسم و شماره جدید
name=input('pls input name==>')
number=input('pls input number of'+name+"==>")
#اضافه کردن شماره و اسم جدید به دیکشنری
number_dict[name]=number
#وارد کردن یک اسم برای پیدا کردن شماره آن از دفترچه
name_search=input('pls input name for search number==>')
# پیدا کردن شماره یک فرد از دیکشنری
print(number_dict[name_search])
if number_dict[name_search]:
    print('yesssssss')
else:
    print('nooooooo')


