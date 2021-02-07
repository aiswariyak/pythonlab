gcd=1
n=int(input("enter the  first number"))
m=int(input("enter the second number"))
if(n>m):
    for i in range(1,n+1):
        if n%i==0 and m%i==0:
            gcd=i
if(m>n):
    for i in range(1,m+1):
        if n%i==0 and m%i==0:
            gcd=i
print("the gcd of %d and %d is %d" %(n,m,gcd))


            
            
            
