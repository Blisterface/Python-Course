def prime(bound:int):
    for number in range(2,bound):
        for i in range(2,number//2):
            if number % i == 0:
                break
        else:
            yield number


gen = prime(20)
while gen:
    print(next(gen))
#print(list(gen))