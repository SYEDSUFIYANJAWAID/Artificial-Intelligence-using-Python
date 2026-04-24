class Student:
    @staticmethod
    def percentage(marks,total):   #stactmethod
        return (marks / total) * 100


    school = "ssj School"   # class attribute
    
    
    def __init__(self ,name,marks):
        self.name=name #instance attribute
        self.marks=marks  #instance attribute

    def show(self):
        print("NAME:",self.name)
        print("SCHOOL NAME:",self.school) #method
        print("marks:",self.marks)
    
    def greet(self):                   #method
        print("Hello", self.name)
  


s1 = Student("sufiyan",77)
s1.greet()
print("Percentage:", Student.percentage(s1.marks, 100))
s1.show()


