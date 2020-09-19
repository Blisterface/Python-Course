some_list = ['a','b','c','d','m','n','n','b']
duplicate_list=[]
for x in some_list:
    if some_list.count(x)>1:
        if(duplicate_list.count(x)==0):
            duplicate_list.append(x)
            
print(duplicate_list)