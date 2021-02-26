import graphics
from graphics import circle
from graphics.rectangle import*
from graphics.threedgraphics import cuboid,sphere
radius=int(input("enter the radius of circle:"))
print("area of circle is %.3f" %(circle.area(radius)))
print("perimeter of circle is %.3f:" %(circle.perimeter(radius)))
length=int(input("enter the length of rectangle"))
breadth=int(input("enter the breadth of rectangle"))
print("area of rectangle:",rect_area(length,breadth))
print("perimeter of rectangle:",rect_perimeter(length,breadth))
length=int(input("enter the length of cuboid"))
breadth=int(input("enter the breadth of cuboid"))
height=int(input("enter the height of cuboid"))
print("area of cuboid:",cuboid.cuboid_area(length,breadth,height))
print("perimeter of cuboid:",cuboid.cuboid_perimeter(length,breadth,height))
radius=int(input("enter the radius of sphere:"))
print("area of sphere is %.3f" %(sphere.sphere_area(radius)))
print("perimeter of sphere is %.3f:" %(sphere.sphere_perimeter(radius)))






