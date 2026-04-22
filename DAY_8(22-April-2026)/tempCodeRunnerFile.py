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