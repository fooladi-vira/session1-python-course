def check(grade):
    if grade>=10:
        return True
    elif grade<10:
        return False
    
a=int(input("pls enter your grade==>"))
a_result=check(a)

if a_result==True:
    print("good")
else:
    print("bad")



