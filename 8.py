import random
i=random.randint(1,10)
names={}
for key in range(11):#[1,2,3,4,5,6,7,8,9,10]
    name=input('pls input name ==>')
    names[key]=name
print(i,names[i])