from time import time
user1 ={
    'name':'Sorna',
    'valid':True
}
def authenticated(func):
    def wrapper_func(*args,**kwargs):
        if user1['valid']==True:
            func(*args,*kwargs)
    return wrapper_func

@authenticated
def message_friend(user):
    print('Message has been sent')

message_friend(user1)

def perfomance(func):
    def wrapper(*args,**kwargs):
        t1 = time()
        result = func(*args,**kwargs)
        t2 = time()
        print(f'timer took {t2-t1} s')
        return result
    return wrapper

@perfomance
def long_time():
    for i in range(100000000):
        i*5

long_time()