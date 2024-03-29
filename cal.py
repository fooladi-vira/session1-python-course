a=input('enter number 1==>')
alamat=input('alamat==>')
b=input('enter number 2==>')

def mycal(a,b,almat):
    if alamat=='*':
        result=int(a)*int(b)   
    if alamat=='/':
        if int(b)==0:
            print('error')
        else:
            result=int(a)/int(b)  
    if alamat=='+':
        result=int(a)*+int(b) 
    if alamat=='-':
        result=int(a)-int(b) 
    print(result)

mycal(a,b,alamat)
mycal(5,9,'+')
mycal(5,9,'-')
