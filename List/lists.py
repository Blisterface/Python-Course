#lists: ordered, mutable, allows duplicate elements

my_list = ['Banana','Cherry', 'Apple']
my_list2 = [5,2,6,7,3,4,1]
#not in order sorting
new_list =sorted(my_list2)
print(my_list2)#displays the original unsorted list
print(new_list)
#in order sorting O(nlogn)
my_list2.sort()
#removes and return the last element in the list
item = my_list.pop()
#insert an item in the given index
my_list.insert(1,'Orange')
#insert an item at the end of the list
my_list.append("Pineaple")
print(my_list2)
#create a list with the same elements
another_list = [1]*5
print(another_list)
#concatenate different lists
conc_list = my_list + new_list
print(conc_list)
#list slicing
sliced_list = conc_list[3:7]
print(sliced_list)
#copy list
list_copy = my_list #both lists refer to the same memory
list_copy.append('Guava')
print(list_copy)
print(my_list)
#proper copy. you can also use the 'list' function or slicing
my_list.remove('Guava')
list_copy = my_list.copy()# list copy now pointing to new address
list_copy.append('Guava')
print(my_list)
print(list_copy)
# list comprehension
a = [1,2,3,4,5,6]
b = [x*x for x in a]
print(b)