string=input("enter the line of text")
l=string.split()
set_=list(set(l))
for i in set_:
    print(l.count(i),"is the count of",i)
