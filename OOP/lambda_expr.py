my_list = [3,4,5]
#mulitply each value in the list by two
print(list(map(lambda item: item*2,my_list)))

another_list = [1,2,3,4,5]
# Square each value in the list
print(list(map(lambda item: item**2,another_list)))

a= [(3,8),(0,2),(4,3),(9,8),(10,-1)]
a.sort(key=lambda x: x[1])
print(a)
