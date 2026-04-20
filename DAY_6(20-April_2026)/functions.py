def greet():
    print("hello")

greet()


#with parameters 
def add_two_numbers(a,b):
    return a+b
                              #return function ma ap values store karwa sakte han                            
x =add_two_numbers(2, 3)
print(x)



def add_two_numbers1(a,b):
    print(a+b)

add_two_numbers(6,7)
add_two_numbers1(6,7)

def check_numbers(a):
    num=[]
    total_sum=0
    num.append(a)
    total_sum=total_sum+a

# Requirements:
# function multiple numbers lega (list form me)
# list me se:
# even numbers count karo
# odd numbers count karo
# total sum nikalo

def check_numbers():
 a=int(input("enter a number"))
 total_sum=0
 num=[]
 while a>=0:
  num.append(a)
  total_sum=total_sum+a
  a=int(input("enter a number"))
 

 print(total_sum)
 print(num)
 even_list=[]
 odd_list=[]
 even_count=0
 odd_count=0
 for items in num:
    if items%2==0: 
     even_list.append(items) 
     print(items,"even")
     even_count += 1 
    elif items%2==1:
        odd_list.append(items)
        print(items,"odd")
        odd_count += 1
      

 print("Even Count:", even_count)
 print("Odd Count:", odd_count)

