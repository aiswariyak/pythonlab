y=int(input("enter the year"))
if y%400==0 or(y%100!=0 and y%4==0):
    print(y,"is leap year")
else :
    print(y,"is not a leap year")
