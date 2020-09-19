from functools import reduce

my_list = [3,5,6,4,8,7,11,9]
your_list = [1,2,8,7,11,9]
def mult_by_two(item):
    return item*2
def only_odd(item):
    return item%2!=0

def accumulator(acc,item):
    #print(acc,item)
    return acc + item

# Capitalise all the name in the list
def capitalise(item):
    return item.capitalize()

# filter values above a given number
def above_num(item):
    return item>50

my_pets =['sisi','bibi','titi','carla']
scores = [73,20,65,19,76,100,88]
passed = list(filter(above_num,scores))
pets = list(map(capitalise,my_pets))
print(pets)
print(passed)

my_strings = ['a','b','c','d','e']
my_numbers = [5,3,4,1,2]
my_numbers.sort()

print(list(zip(my_numbers,my_strings)))
combined = my_numbers + scores
#new_list = list(map(mult_by_two,my_list))
#odd_list = list(filter(only_odd,my_list))
#print(new_list)
#print(odd_list)
#print(list(zip(my_list,your_list)))
print(reduce(accumulator,combined))