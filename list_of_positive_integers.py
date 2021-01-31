n=int(input("enter the length of list"))
l=[]
for i in range(n):
    ele=int(input("enter the element"))
    l.append(ele)
print("the list of integers:")
print(l)    
lp=[ i for i in l if i>=0 ]
print("list of positive integers:")
print(lp)
