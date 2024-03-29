student={1:'zahra',2:'ali','A':'ali',4:'mohamad'}
print(student)
print(student.keys())
print(student.values())
#ویرایش کردن مقدار کلید A
student['A']='Vira'
print(student)
#حذف کردن از دیکشنری
del student[1]
print(student)
student.clear()
print(student)