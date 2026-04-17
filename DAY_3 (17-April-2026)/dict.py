
student7 = {"name": "Ali", "age": 22, "dept": "CS"}

print(student7.get("name"))
print(student7.get("salary", "Not Found"))

student7.update({"age": 23, "city": "Lahore"})
student7["cgpa"] = 3.5

print(student7.keys())
print(student7.values())
print(student7.items())

for k, v in student7.items():
    print(k, ":", v)

student7.pop("age")
student7.popitem()

new_student = student7.copy()
print(new_student)

student7.clear()
print(student7)

#nested dictory
data = {
    "student1": {"name": "Ali", "age": 22},
    "student2": {"name": "Ahmed", "age": 23}
}

print(data["student1"]["name"])


# C3. Dictionary Basics
# student = {
#     "name": "Ali",
#     "age": 22,
#     "dept": "CS"
# }
# age update karo (23)
# new key add karo: "cgpa": 3.5

student = {
    "name": "Ali",
    "age": 22,
    "dept": "CS"
}

student["age"]=23
student["Cgpa"]=3.5
print(student)

# C4. Loop through Dictionary
# Student dictionary ke keys aur values print karo.
student = {
    "name": "Ali",
    "age": 22,
    "dept": "CS"
}
print(student.items())

student = {
    "name": "Ali",
    "age": 22,
    "dept": "CS"
}
print(student.keys())
print(student.values())
print(student.items())
for key, value in student.items():
    print(key, ":", value)



# C5. Mini Automation Data
# employees = [
#     {"name": "Ali", "salary": 50000},
#     {"name": "Sara", "salary": 70000},
#     {"name": "Usman", "salary": 60000}
# ]
# Sab employees ke naam print karo
# Jinka salary > 60000 ho unka naam print karo

employees = [
    {"name": "Ali", "salary": 50000},
    {"name": "Sara", "salary": 70000},
    {"name": "Usman", "salary": 60000}
]
print(employees[0].keys())


for names in employees:
    print(names["name"])


    if(names["salary"]>60000):
     print("name:",names["name"],"\nSalary" ,names["salary"])       


products = [
    {"name": "Laptop", "price": 120000, "stock": 5},
    {"name": "Mouse", "price": 1500, "stock": 0},
    {"name": "Keyboard", "price": 3500, "stock": 12},
    {"name": "Monitor", "price": 30000, "stock": 2}
]

Total_stock = 0

for product in products:
    print(product["name"])

    # Stock 0 check
    if product["stock"] <= 0:
        print(product["name"], "Has 0 stock")

    # Price > 10000
    if product["price"] >= 10000:
        print(product["name"], ":", product["price"])
       

    # Total stock update
    Total_stock = Total_stock + product["stock"]

print("Total Stock:", Total_stock)



dict={
        "name": "Laptop",
        "price": 120000,
        "stock": 5
    }

dict["price"]=50000
dict.pop("name")
print(dict)