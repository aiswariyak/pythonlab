d1=dict()
n=int(input("enter the total no of elements in the first dictionary"))
for i in range(n):
    item=int(input("enter the value"))
    d1[i]=item
print(d1)
d2=dict()
m=int(input("enter the total no of elements in the second dictionary"))
for i in range(4,4+m):
    item=int(input("enter the value"))
    d2[i]=item
print(d2)
for i in d2:
    if i in d1:
        d1[i]+=d2[i]
    else:
        d1[i]=d2[i]
print("merged dictionary:")        
print(d1)        
