one_side=int(input("enter the side of square"))
square_area=lambda a:a*a
print("area of square:",square_area(one_side))
length=int(input("enter the length"))
breadth=int(input("enter the breadth"))
rect_area=lambda l,b:l*b
print("area of rectangle:",rect_area(length,breadth))
length=int(input("enter the height of triangle"))
breadth=int(input("enter the breadth of triangle"))
triangle_area=lambda h,b:(1/2)*b*h
print("area of triangle is %.2f" %(triangle_area(length,breadth)))
