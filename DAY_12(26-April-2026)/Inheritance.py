# Hard Question: Multi-Level + Override
# 🎯 Task:
# 3 classes banao:
# 1. Person
# attributes:
# name
# method:
# show() → print name
# 2. Student (inherits from Person)
# attributes:
# marks
# method:
# show() → print name + marks
# 3. Topper (inherits from Student)
# attributes:
# rank
# method:
# show() → print name + marks + rank
# ❗ Rules:
# super() use karna zaroori hai
# method override karna hai har class me
# constructor properly chain hona chahiye
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def show(self):
        super().show()
        print("Marks:", self.marks)


class Topper(Student):
    def __init__(self, name, marks, rank):
        super().__init__(name, marks)
        self.rank = rank

    def show(self):
        super().show()
        print("Rank:", self.rank)


t1 = Topper("sufiyan", 77, 7)
t1.show()