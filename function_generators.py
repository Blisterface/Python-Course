#Functtion generators
def gen_func(num):
    for i in range(num):
        yield i

for item in gen_func(50):
    print(item/2,end=' ')
