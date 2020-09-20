#Functtion generators
def gen_func(num):
    for i in range(num):
        yield i

for item in gen_func(101):
    print(item,end=' ')
print()