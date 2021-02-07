def fact(n):
    f=1;
    for i in range(n,0,-1):
        f=f*i;
    return f
n=int(input("enter the number"))
print("factorial of %d is %d" %(n,fact(n)))
