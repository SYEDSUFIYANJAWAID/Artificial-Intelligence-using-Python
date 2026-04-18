for i in range(1, 21):

    if i == 7:
        continue      

    if i == 15:
        break         

    print(i)

#continune
for i in range(1, 11):

    if i % 2 != 0:
        continue   # odd numbers skip karega

    print(i)

#break
for i in range(1, 11):

    if i == 5:
        break   # 5 par loop ruk jayega

    print(i)

#we can use with if,else in for loop  
for i in range(5):
    if i == 3:
        break
    print(i)

#method for loop 

#with range
num = 3

for i in range(1, 11):          #print tabel by for loop
    print(num, "x", i, "=", num * i)

#with list 
fruits = ["apple", "banana", "mango"]

for item in fruits:
    print(item)

#with string
name = "sam"

for ch in name:
    print(ch)

#index and value both print method
fruits = ["apple", "banana", "mango"]

for index, value in enumerate(fruits):
    print(index, value)

# multiple  list ke saat
names = ["Ali", "Sara"]
marks = [80, 90]

for n, m in zip(names, marks):
    print(n, m)