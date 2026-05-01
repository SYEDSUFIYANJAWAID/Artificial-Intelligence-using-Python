a=3
b=7
print(a+b)

c="sufi"
b="yan"
print(c+b) #string ko jorna concatenate

e=[7,3,2]
d=[7,34,5]
result_list=print(e+d) 
print(type(result_list)) #merge

import math


class shape:

    def speak(self):
        print("this is shape")
    


class circle(shape):

    def areaofcircle(self,r):
        self.areacircle=math.pi * r*2
        print("the area of circle:",self.areacircle)


class square(shape):

    def areaofsquare(self,r):
         self.squarearea= r*r
         print("the area of square:",self.squarearea)

c1=circle()
c1.speak()
c1.areaofcircle(5)
s1=square()
s1.speak()
s1.areaofsquare(8)