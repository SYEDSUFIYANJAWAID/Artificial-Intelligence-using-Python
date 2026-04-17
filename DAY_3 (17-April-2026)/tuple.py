tup=(22,44,77,22)
#tup[2] = 100 #not allowed tuple are immutabel
print(tup)



data = (10, 20, 30, 40)
print(data[2]) #with index
print(data[(len(data)-1)]) #with len

student1 = ("Ali", 22, "CS")
name1=student1[0]
age1=student1[1]
dept1=student1[2]
print("name: ",name1,"\nage:",age1,"\ndept: ",dept1)

# P1. Ek tuple banao jisme 5 cities ho
# P2. Tuple ka length print kar
tup2=("karachiu","lahore","islamambad","pindhi","KpK")
print(len(tup))

#methoddes of tuple 
print(tup.index(44)) #print 1 becausr 44 is on 1 index

print(tup.count(22))

#tuple unpacking another example
student = ("Ali", 22, "CS")

name, age, dept = student
print(name , age , dept)