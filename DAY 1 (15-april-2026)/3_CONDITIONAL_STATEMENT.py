a=int(input("enter a number: "))
if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("Zero")

b=int(input("enter Your Marks: "))
if (b>80 and b<=100):
  print("A")
elif(b>60 and b<=79):
   print("B")
elif(b>40 and b<=59):
   print("c")
else:
   print("FAil")

username="admin"
password=1234
username1=input("Enter user name:")
Password1=int(input("Enter password:"))
if (username==username1 and  password==Password1):
  print("login successful")
else:
  print("Access denied")