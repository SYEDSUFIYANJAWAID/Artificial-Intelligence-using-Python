#agar answer ko store karwana kisi varibel ma to return use karo
def double_number_with_return(a):
    return a*2

print(double_number_with_return(10))
q=double_number_with_return(5)
print(q)

#agar answer ko store nhi karwana to print use karo
def double_number(a):
    print(a*2)
double_number(5)

#with lamda simple and clean usin for small task and with map and filter
double=lambda x:x*2
print(double(5))

#add two nambers
add = lambda a, b: a + b
print(add(2, 3))


#map with lambda
numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)
print(list(result))

things = ["cake", "biscuits", "bread"]
result = list(map(lambda x: x.upper(), things))
print(result)

#loop
capital_names_list=[]
things = ["cake", "biscuits", "bread"]
for names in things:
    capital_names=names.upper()
    capital_names_list.append((capital_names))
    
print(capital_names_list)


#filter with lambda
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)


#with loop
nums_even_list=[]
num=[1, 2, 3, 4, 5, 6]
for items in num:

    if items%2==0:
     nums_even_list.append(items)

print(nums_even_list)

data = [10, -5, 20, -2, 0]
result = list(filter(lambda x: x > 0, data))
print(result)

names = ["Ali", "Ahmad", "Usman", "A"]
result = list(filter(lambda x: len(x) > 3, names))
print(result)