#list comprehensions
my_list = [num*3 for num in range(0,20) if num%2==0]
#print(my_list)

my_dict = {num:num*2 for num in [1,2,3,4]}
#print(my_dict)

dup_list = ['a','b','c','b','d','n','m','n']
dup = set([x for x in dup_list if dup_list.count(x)>1])
print(list(dup))