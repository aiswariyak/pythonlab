def fibonacci(n):
    a=1
    b=0
    c=0
    count=0
    while(count!=n):
        print(c,end=",")
        c=a+b
        a=b
        b=c
        count=count+1
n=int(input("enter the range"))
fibonacci(n)
        
