
def myCal(a,b,op):
    if op=='+':
        return a+b
    if op=='-':
        return a-b
    if op=='*':
        return a*b
    if op=='/':
        return a/b
    if op=='%':
        return a%b
a=input('enter number 1==>')
alamat=input('alamat==>')
b=input('enter number 2==>')
s=myCal(int(a),int(b),alamat)
print(s)
