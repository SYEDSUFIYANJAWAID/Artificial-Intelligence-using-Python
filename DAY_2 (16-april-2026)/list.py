# C1.
# Ek list banao:
# numbers = [10, 20, 30, 40, 50]
# 30 print karo
# last element print karo

list_2=[10,20,30,40,50]
print(list_2[2])
print(list_2[4])


# C2.
# Ek list:
# names = ["table", "chair", "fan", "light"]
# "fan" remove and pop karo
# "bulb" add karo

#with pop method
Names=["table", "chair", "fan", "light"]
Names.pop(2)
print(Names)
#Names.append("bulb") #last ma add
Names.insert(2,"bulb")
print(Names)

#with remove method
Names=["table", "chair", "fan", "light"]
Names.remove("fan")
print(Names)
#Names.append("bulb") #last ma add
Names.insert(2,"bulb")
print(Names)


# C5.
# List:
# marks = [45, 78, 88, 32, 90]
# highest marks print karo
# lowest marks print karo

marks = [45, 78, 88, 32, 90]
print(max(marks))
print(min(marks))


# P1. Ek empty list banao aur 3 sweets names add karo
sweets=[]
sweets.append("cake")
sweets.append("pastries")
sweets.append("Gulab jamun")
print(sweets)
#with index
print(sweets[2])
# P2. List ka length print karo
print(("the length of sweets list is:",len(sweets)))
# P3. List ko ascending order mein sort karo
sweets.sort()
print(("the sort (ascending order)  of sweets list is:",sweets))
# P4. List ka second last element print karo
print(sweets[len(sweets)-1])

# P5. List ko reverse order mein print karo
sweets.sort(reverse=True)
print(("the reverse of sweets list is:",sweets))

#count method
print(("the word cake in sweets list is :",sweets.count("cake"))) #eturns a number or cake word appers in list

#copy method
copy_of_sweets=sweets.copy()
print(("the copy of sweets list is:",copy_of_sweets))

#how to check a list is copy or not
print(id(sweets))
print(id(copy_of_sweets))   # Agar id same ho → same list
                            #Agar id different ho → copy list

#slicing
num=[14,24,36,45,57,60,77,28,59]
print(num[1:6]) # index 1 se 5 (index 6 nhi ayegs)
print(num[:6])  #index 0 se 5 ( 6 not included)
print(num[1:])  #index 0 nhi bakii sab
print(num[:])  #full list
print(num[::2])  # 2nd element uthata hai
print(num[-3:-1]) #End se count hota hai
#num=[14(-9),24,36,45,57,60,77,28(-2),59(-1)]
#-1 right se index numbers hote han example uper deklen
print(num[::-1])#revers hojayega

a = [1,2,3,4]
a[1:3] = [9,9] #use slicling to change list numbers
print(a)  # [1,9,9,4]

del a[1:3] #delete using slicing
