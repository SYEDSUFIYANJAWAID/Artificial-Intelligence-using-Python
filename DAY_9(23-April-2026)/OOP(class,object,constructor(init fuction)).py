class student_exam_result:
    result="pass"

s1=student_exam_result()
s2=student_exam_result()
s3=student_exam_result()

print(s1.result)
print(s2.result)
print(s3.result)

#s1, s2, s3 = student_exam_result(), student_exam_result(), student_exam_result()
# print(s1.result, s2.result, s3.result)
# do in one line 

#constructor
class car:
    def __init__(self , brand_name , model):
      self.brand_name= brand_name
      self.model=model


car1=car("SSJ" , 2026)
print(car1.brand_name,car1.model)

# Question (Constructor Practice)
# 👉 Ek class banao: Student
# 🎯 Requirements:
# __init__ me 2 cheeze lo:
# name
# marks
# Ek method banao show()
# print kare:

class student:
    def __init__(self , name , marks):
      self.name= name
      self.marks=marks

student1=student("ssj" ,77)
print("Name:",student1.name ,"\nMarks:",student1.marks)

#with show method
class student:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

student1 = student("ssj", 77)
student1.show()