import math
a=float(input("Enter side a: "))
b=float(input("Enter side b: "))
c=float(input("Enter side c: "))
if(a+b>c)and(a+c>b)and(b+c>a):
    
 s=(a+b+c)/2
 area=math.sqrt(s*(s-a)*(s-b)*(s-c))
 print("The area of the triangle is: " ,round(area))
else:
    print("The given sides do not form a valid triangle.")
    