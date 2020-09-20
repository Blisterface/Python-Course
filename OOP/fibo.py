def gen(num):
    for i in range(num):
        yield i

def fibo(num):
    a =0
    b=1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + a 

for x in fibo(20):
    print(x)