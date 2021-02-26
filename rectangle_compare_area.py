class rectangle:
        def __init__(self,l,w):
              self.__len=l
              self.__wid=w
        def __lt__(self,other):
                a1=self.__len * self.__wid
                a2=other.__len * other.__wid
                if a1<a2:
                        return True
                else:
                        return False
l1=int(input("enter the length of first rectangle"))
w1=int(input("enter the width of first rectangle"))
r1=rectangle(l1,w1)
l2=int(input("enter the length of second rectangle"))
w2=int(input("enter the width of second rectangle"))
r2=rectangle(l2,w2)
if r1<r2:
        print("the second rectangle has largest area")
else:
        print("the first rectangle has largest area")
        

            
            
            
            
        
