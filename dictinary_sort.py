d={}
n=int(input("enter range"))
for i in range(n):
    key=input("enter the key")
    value=input("enter the value")
    d[key]=value
print("dictionary in ascending order:")
asc=sorted(d.items())
print(asc)
print("dictionary in descending order:")
asc.reverse()
print(asc)
