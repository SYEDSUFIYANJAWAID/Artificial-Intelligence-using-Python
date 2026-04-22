#Normal list
numbers3 = [1, 2, 3, 4]
squares = []
for i in numbers3:
    squares.append(i*i)
print("output of list loop")
print(squares)

#list Comprehension:
numbers2 = [1, 2, 3, 4]
squares = [i*i for i in numbers2] #simple
print("output of list comprehension")
print(squares)

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [i*i for i in numbers1 if i % 2 == 0 and i > 5] #if (with )condition

#question for understanding list comprehension
# List comprehension use karke:
# Agar number even ho uska square lo
# Agar number odd ho uska cube lo
numbers4=[1,2,3,4,5,6]
even_odd_double_list_by_loop=[]
square_num=0
cube_num=0
for items in numbers4:
  if items%2==0:
    square_num=items*items
    even_odd_double_list_by_loop.append(square_num)
  else:
    cube_num=items*items*items
    even_odd_double_list_by_loop.append(cube_num)

print(even_odd_double_list_by_loop)

#another 
numbers4=[1,2,3,4,5,6]
even_odd=[]
for items in numbers4:
  if items%2==0:
    even_odd.append(items*items)
  else:
    # cube_num=items*items*items
    even_odd.append(items*items*items)

print(even_odd)


numbers = [1,2,3,4,5,6] 
even_odd_double_list=[i*i if i%2==0 else i*i*i for i in numbers] #if-else
print(even_odd_double_list)

# ADvance conpect 
# 1.Nested list comprehension
# 2.Nested with condition
# 3.Matrix / 2D List Comprehension
# 4.With function call

# dont need to learn then as these are advvance concept with time we learn it by own