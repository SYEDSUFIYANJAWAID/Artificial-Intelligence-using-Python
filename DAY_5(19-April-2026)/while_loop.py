i = 1

while i <= 5: #kab tak condition chlanai ha 
    print(i)
    i += 1 #ye likha zroori warna loop chalta rahe ga (crash)


i = 1

while i <= 5:
    print(i) # i+=1 agar nhi lagae to else lagao take loop band hogye 
else:           #also use break to stop a loop else tab chalta hai jab loop normally end ho (break na lage)
    print("loop ended")

i = 5

while i > 0:
    print(i)
    i -= 1 #minus ma bhi likh sakte han 

i = 0

while i < 5:
    i += 1
    if i == 3:
        continue #jab skip karna ho
    print(i)


#example
password = ""

while password != "1234":
    password = input("Enter password: ")

print("Access Granted")

# Ek program banao jo user se numbers input leta rahe
# 👉 Jab tak user negative number (-1 ya koi bhi negative) na dale, program chalta rahe
# 👉 Jab negative number aaye → loop stop ho jaye
# 👉 Aur total sum print kare



while num1 != -1:
    total_sum = total_sum + num1
    num1 = int(input("Enter number: "))

print("Total Sum:", total_sum)
print("Don't enter negative numbers")